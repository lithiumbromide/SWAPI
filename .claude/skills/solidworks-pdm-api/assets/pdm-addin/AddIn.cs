using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using EPDM.Interop.epdm;
[assembly: ComVisible(false)]
namespace PdmAddIn
{
    [Guid("00000000-0000-0000-0000-000000000000"), ComVisible(true)]
    public class AddIn : IEdmAddIn5
    {
        private const string Caption = "PDM add-in";
        private const int ShowPathsCommand = 1000;
        private const string GuardedState = "Released";
        private const string RequiredVariable = "Checked By";
        public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
        {
            poInfo.mbsAddInName = Caption;
            poInfo.mbsCompany = "Company";
            poInfo.mbsDescription = "Shows local paths and blocks transitions with missing card values";
            poInfo.mlAddInVersion = 1;
            poInfo.mlRequiredVersionMajor = 10;
            poInfo.mlRequiredVersionMinor = 0;
            poCmdMgr.AddCmd(ShowPathsCommand, "Show local paths", (int)(EdmMenuFlags.EdmMenu_MustHaveSelection | EdmMenuFlags.EdmMenu_OnlyFiles), "Shows the local paths of the selected files", "Show local paths");
            poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreState);
        }
        public void OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
        {
            var vault = (IEdmVault5)poCmd.mpoVault;
            var items = ppoData ?? new EdmCmdData[0];
            try
            {
                if (poCmd.meCmdType == EdmCmdType.EdmCmd_Menu && poCmd.mlCmdID == ShowPathsCommand)
                {
                    ShowPaths(vault, poCmd, items);
                }
                else if (poCmd.meCmdType == EdmCmdType.EdmCmd_PreState)
                {
                    GuardTransition(vault, ref poCmd, items);
                }
            }
            catch (COMException ex)
            {
                if (poCmd.meCmdType == EdmCmdType.EdmCmd_PreState)
                {
                    poCmd.mbCancel = 1;
                }
                Report(vault, poCmd, Describe(vault, ex));
            }
        }
        private static void ShowPaths(IEdmVault5 vault, EdmCmd cmd, EdmCmdData[] items)
        {
            var paths = new List<string>();
            foreach (var item in items)
            {
                if (item.mlObjectID1 != 0)
                {
                    paths.Add(item.mbsStrData2);
                }
            }
            Report(vault, cmd, string.Join(Environment.NewLine, paths));
        }
        private static void GuardTransition(IEdmVault5 vault, ref EdmCmd cmd, EdmCmdData[] items)
        {
            var missing = new List<string>();
            foreach (var item in items)
            {
                if (!string.Equals(item.mbsStrData2, GuardedState, StringComparison.OrdinalIgnoreCase))
                {
                    continue;
                }
                var file = (IEdmFile5)vault.GetObject(EdmObjectType.EdmObject_File, item.mlObjectID1);
                if (string.IsNullOrWhiteSpace(ReadVariable(file, RequiredVariable)))
                {
                    missing.Add(item.mbsStrData1);
                }
            }
            if (missing.Count == 0)
            {
                return;
            }
            cmd.mbCancel = 1;
            Report(vault, cmd, RequiredVariable + " is empty, transition to " + GuardedState + " refused:" + Environment.NewLine + string.Join(Environment.NewLine, missing));
        }
        private static string ReadVariable(IEdmFile5 file, string name)
        {
            var variables = (IEdmEnumeratorVariable8)file.GetEnumeratorVariable();
            try
            {
                object value;
                if (!variables.GetVar(name, "@", out value))
                {
                    variables.GetVar(name, "", out value);
                }
                return Convert.ToString(value);
            }
            finally
            {
                variables.CloseFile(false);
            }
        }
        private static void Report(IEdmVault5 vault, EdmCmd cmd, string message)
        {
            if (cmd.mbSilentMode == 0)
            {
                vault.MsgBox(cmd.mlParentWnd, message, EdmMBoxType.EdmMbt_OKOnly, Caption);
            }
        }
        private static string Describe(IEdmVault5 vault, COMException ex)
        {
            string name;
            string description;
            vault.GetErrorString(ex.ErrorCode, out name, out description);
            return string.Format("0x{0:X8} {1}: {2}", ex.ErrorCode, name, description);
        }
    }
}
