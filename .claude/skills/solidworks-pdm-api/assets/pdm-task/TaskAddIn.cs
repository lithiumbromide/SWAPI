using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Runtime.InteropServices;
using System.Threading;
using EPDM.Interop.epdm;
using SolidWorks.Interop.swdocumentmgr;
[assembly: ComVisible(false)]
namespace PdmTask
{
    [Guid("00000000-0000-0000-0000-000000000000"), ComVisible(true)]
    public class TaskAddIn : IEdmAddIn5
    {
        private const string CheckInComment = "Card variables updated from custom properties by task add-in";
        private const string LicenseKeyVariable = "SW_DM_LICENSE_KEY";
        private static readonly IDictionary<string, string> PropertyToVariable = new Dictionary<string, string>
        {
            { "DrawnBy", "DrawnBy" },
            { "DrawnDate", "DrawnDate" }
        };
        public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
        {
            poInfo.mbsAddInName = "PDM task add-in";
            poInfo.mbsCompany = "Company";
            poInfo.mbsDescription = "Copies custom properties of the selected SOLIDWORKS files into card variables on a task host";
            poInfo.mlAddInVersion = 1;
            poInfo.mlRequiredVersionMajor = 10;
            poInfo.mlRequiredVersionMinor = 0;
            poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskSetup);
            poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskLaunch);
            poCmdMgr.AddHook(EdmCmdType.EdmCmd_TaskRun);
        }
        public void OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
        {
            var items = ppoData ?? new EdmCmdData[0];
            switch (poCmd.meCmdType)
            {
                case EdmCmdType.EdmCmd_TaskSetup:
                    OnTaskSetup((IEdmTaskProperties)poCmd.mpoExtra);
                    break;
                case EdmCmdType.EdmCmd_TaskLaunch:
                    if (items.Length == 0)
                    {
                        poCmd.mbCancel = 1;
                    }
                    break;
                case EdmCmdType.EdmCmd_TaskRun:
                    OnTaskRun((IEdmVault5)poCmd.mpoVault, (IEdmTaskInstance)poCmd.mpoExtra, items);
                    break;
            }
        }
        private static void OnTaskSetup(IEdmTaskProperties properties)
        {
            properties.TaskFlags = (int)EdmTaskFlag.EdmTask_SupportsInitExec;
            var commands = new EdmTaskMenuCmd[1];
            commands[0].mbsMenuString = "Copy custom properties to card";
            commands[0].mbsStatusBarHelp = "Copies custom properties of the selected SOLIDWORKS files into their card variables";
            commands[0].mlCmdID = 1;
            commands[0].mlEdmMenuFlags = (int)(EdmMenuFlags.EdmMenu_MustHaveSelection | EdmMenuFlags.EdmMenu_OnlyFiles);
            properties.SetMenuCmds(commands);
        }
        private static void OnTaskRun(IEdmVault5 vault, IEdmTaskInstance instance, EdmCmdData[] items)
        {
            try
            {
                instance.SetStatus(EdmTaskStatus.EdmTaskStat_Running);
                var documents = OpenDocumentManager();
                instance.SetProgressRange(items.Length, 0, "Starting");
                var failures = new List<string>();
                for (var i = 0; i < items.Length; i++)
                {
                    if (StopRequested(instance))
                    {
                        return;
                    }
                    var item = items[i];
                    if (item.mlLongData1 == (int)EdmObjectType.EdmObject_File)
                    {
                        try
                        {
                            ProcessFile(vault, documents, item);
                        }
                        catch (Exception ex)
                        {
                            failures.Add(item.mbsStrData1 + ": " + Describe(vault, ex));
                        }
                    }
                    instance.SetProgressPos(i + 1, item.mbsStrData1);
                }
                if (failures.Count == 0)
                {
                    instance.SetStatus(EdmTaskStatus.EdmTaskStat_DoneOK);
                }
                else
                {
                    instance.SetStatus(EdmTaskStatus.EdmTaskStat_DoneFailed, 0, string.Join(Environment.NewLine, failures));
                }
            }
            catch (Exception ex)
            {
                instance.SetStatus(EdmTaskStatus.EdmTaskStat_DoneFailed, ex.HResult, Describe(vault, ex));
            }
        }
        private static bool StopRequested(IEdmTaskInstance instance)
        {
            var status = instance.GetStatus();
            if (status == EdmTaskStatus.EdmTaskStat_SuspensionPending)
            {
                instance.SetStatus(EdmTaskStatus.EdmTaskStat_Suspended);
                while (instance.GetStatus() == EdmTaskStatus.EdmTaskStat_Suspended)
                {
                    Thread.Sleep(1000);
                }
                status = instance.GetStatus();
                if (status == EdmTaskStatus.EdmTaskStat_ResumePending)
                {
                    instance.SetStatus(EdmTaskStatus.EdmTaskStat_Running);
                }
            }
            if (status != EdmTaskStatus.EdmTaskStat_CancelPending)
            {
                return false;
            }
            instance.SetStatus(EdmTaskStatus.EdmTaskStat_DoneCancelled);
            return true;
        }
        private static ISwDMApplication OpenDocumentManager()
        {
            var licenseKey = Environment.GetEnvironmentVariable(LicenseKeyVariable);
            if (string.IsNullOrWhiteSpace(licenseKey))
            {
                throw new InvalidOperationException(LicenseKeyVariable + " is not set for the account that runs the task on this host");
            }
            var application = new SwDMClassFactory().GetApplication(licenseKey);
            if (application == null)
            {
                throw new InvalidOperationException("Document Manager rejected the license key in " + LicenseKeyVariable);
            }
            return application;
        }
        private static void ProcessFile(IEdmVault5 vault, ISwDMApplication documents, EdmCmdData item)
        {
            var file = (IEdmFile5)vault.GetObject(EdmObjectType.EdmObject_File, item.mlObjectID1);
            object version = 0;
            object folder = item.mlObjectID2;
            file.GetFileCopy(0, ref version, ref folder, (int)EdmGetFlag.EdmGet_Simple, "");
            var values = ReadValues(documents, file.GetLocalPath(item.mlObjectID2));
            var configuration = FileLevelConfiguration(file);
            file.LockFile(item.mlObjectID2, 0, (int)EdmLockFlag.EdmLock_Simple);
            IEdmEnumeratorVariable8 variables = null;
            try
            {
                variables = (IEdmEnumeratorVariable8)file.GetEnumeratorVariable();
                foreach (var pair in values)
                {
                    var value = pair.Value;
                    variables.SetVar(pair.Key, configuration, ref value, true);
                }
                variables.CloseFile(true);
                variables = null;
                file.UnlockFile(0, CheckInComment, (int)EdmUnlockFlag.EdmUnlock_Simple, null);
            }
            catch (Exception original)
            {
                try
                {
                    if (variables != null)
                    {
                        variables.CloseFile(false);
                    }
                    file.UndoLockFile(0, true);
                }
                catch (Exception cleanup)
                {
                    throw new InvalidOperationException(Describe(vault, original) + "; the file is still checked out because undoing the check-out failed: " + Describe(vault, cleanup), original);
                }
                throw;
            }
        }
        private static IDictionary<string, object> ReadValues(ISwDMApplication documents, string localPath)
        {
            SwDmDocumentOpenError openError;
            var document = documents.GetDocument(localPath, DocumentType(localPath), true, out openError);
            if (document == null)
            {
                throw new InvalidOperationException("Document Manager cannot open " + localPath + ": " + openError);
            }
            try
            {
                var values = new Dictionary<string, object>();
                foreach (var pair in PropertyToVariable)
                {
                    var stored = StoredName(document.GetCustomPropertyNames(), pair.Key);
                    if (stored == null)
                    {
                        throw new InvalidOperationException("custom property " + pair.Key + " is missing in " + localPath);
                    }
                    SwDmCustomInfoType type;
                    values[pair.Value] = ((ISwDMDocument17)document).GetCustomProperty2(stored, out type);
                }
                return values;
            }
            finally
            {
                document.CloseDoc();
            }
        }
        private static SwDmDocumentType DocumentType(string path)
        {
            switch (Path.GetExtension(path).ToLowerInvariant())
            {
                case ".sldprt":
                    return SwDmDocumentType.swDmDocumentPart;
                case ".sldasm":
                    return SwDmDocumentType.swDmDocumentAssembly;
                case ".slddrw":
                    return SwDmDocumentType.swDmDocumentDrawing;
                default:
                    throw new InvalidOperationException("not a SOLIDWORKS document: " + path);
            }
        }
        private static string StoredName(object names, string wanted)
        {
            var list = names as IEnumerable;
            if (list == null)
            {
                return null;
            }
            foreach (var name in list)
            {
                var text = Convert.ToString(name);
                if (string.Equals(text, wanted, StringComparison.OrdinalIgnoreCase))
                {
                    return text;
                }
            }
            return null;
        }
        private static string FileLevelConfiguration(IEdmFile5 file)
        {
            object latest = 0;
            var configurations = file.GetConfigurations(ref latest);
            var position = configurations.GetHeadPosition();
            while (!position.IsNull)
            {
                if (configurations.GetNext(position) == "@")
                {
                    return "@";
                }
            }
            return "";
        }
        private static string Describe(IEdmVault5 vault, Exception ex)
        {
            var com = ex as COMException;
            if (com == null)
            {
                return ex.Message;
            }
            string name;
            string description;
            vault.GetErrorString(com.ErrorCode, out name, out description);
            return string.Format("0x{0:X8} {1}: {2}", com.ErrorCode, name, description);
        }
    }
}
