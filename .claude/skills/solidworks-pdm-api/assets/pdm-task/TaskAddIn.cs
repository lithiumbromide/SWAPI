using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Threading;
using EPDM.Interop.epdm;
[assembly: ComVisible(false)]
namespace PdmTask
{
    [Guid("00000000-0000-0000-0000-000000000000"), ComVisible(true)]
    public class TaskAddIn : IEdmAddIn5
    {
        private const string CheckInComment = "Updated by task add-in";
        public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
        {
            poInfo.mbsAddInName = "PDM task add-in";
            poInfo.mbsCompany = "Company";
            poInfo.mbsDescription = "Updates card variables of the selected files on a task host";
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
            commands[0].mbsMenuString = "Run PDM task";
            commands[0].mbsStatusBarHelp = "Updates card variables of the selected files";
            commands[0].mlCmdID = 1;
            commands[0].mlEdmMenuFlags = (int)(EdmMenuFlags.EdmMenu_MustHaveSelection | EdmMenuFlags.EdmMenu_OnlyFiles);
            properties.SetMenuCmds(commands);
        }
        private static void OnTaskRun(IEdmVault5 vault, IEdmTaskInstance instance, EdmCmdData[] items)
        {
            try
            {
                instance.SetStatus(EdmTaskStatus.EdmTaskStat_Running);
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
                            ProcessFile(vault, item);
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
        private static void ProcessFile(IEdmVault5 vault, EdmCmdData item)
        {
            var file = (IEdmFile5)vault.GetObject(EdmObjectType.EdmObject_File, item.mlObjectID1);
            object version = 0;
            object folder = item.mlObjectID2;
            file.GetFileCopy(0, ref version, ref folder, (int)EdmGetFlag.EdmGet_Simple, "");
            var values = ReadValues(file.GetLocalPath(item.mlObjectID2));
            if (values.Count == 0)
            {
                return;
            }
            var configuration = FileLevelConfiguration(file);
            file.LockFile(item.mlObjectID2, 0, (int)EdmLockFlag.EdmLock_Simple);
            try
            {
                var variables = (IEdmEnumeratorVariable8)file.GetEnumeratorVariable();
                foreach (var pair in values)
                {
                    var value = pair.Value;
                    variables.SetVar(pair.Key, configuration, ref value, true);
                }
                variables.CloseFile(true);
                file.UnlockFile(0, CheckInComment, (int)EdmUnlockFlag.EdmUnlock_Simple, null);
            }
            catch
            {
                file.UndoLockFile(0, true);
                throw;
            }
        }
        private static IDictionary<string, object> ReadValues(string localPath)
        {
            return new Dictionary<string, object>();
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
