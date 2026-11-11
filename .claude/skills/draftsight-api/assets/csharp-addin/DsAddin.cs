using System;
using System.Runtime.InteropServices;
using DraftSight.Interop.dsAddin;
using DraftSight.Interop.dsAutomation;
namespace DraftSightAddin
{
    [ComVisible(true)]
    [Guid("00000000-0000-0000-0000-000000000000")]
    public class Addin : DsAddin
    {
        private const string GlobalName = "_ADDCIRCLE";
        private const string LocalName = "ADDCIRCLE";
        private const string MenuName = "My Add-in";
        private Application dsApp;
        private string apiUuid;
        private Command command;
        private UserCommand userCommand;
        public bool ConnectToDraftSight(object DsApp, int Cookie)
        {
            if (GetType().GUID == Guid.Empty)
            {
                return false;
            }
            dsApp = DsApp as Application;
            if (dsApp == null)
            {
                return false;
            }
            apiUuid = GetType().GUID.ToString();
            dsCreateCommandError_e error;
            command = dsApp.CreateCommand4(apiUuid, GlobalName, LocalName, 0, 0, out error);
            if (command == null || error != dsCreateCommandError_e.dsCreateCommand_Succeeded)
            {
                return false;
            }
            command.ExecuteNotify += OnExecute;
            AddMenu();
            return true;
        }
        public bool DisconnectFromDraftSight()
        {
            if (command != null)
            {
                command.ExecuteNotify -= OnExecute;
            }
            if (dsApp != null)
            {
                dsApp.RemoveUserInterface(apiUuid);
            }
            command = null;
            userCommand = null;
            dsApp = null;
            return true;
        }
        private void AddMenu()
        {
            dsCreateCommandError_e error;
            userCommand = dsApp.CreateUserCommand(apiUuid, "Add circle", "^C^C" + GlobalName, "Adds a circle at a picked point", "", "", dsUIState_e.dsUIState_Document, out error);
            if (userCommand == null || error != dsCreateCommandError_e.dsCreateCommand_Succeeded)
            {
                return;
            }
            WorkSpace workspace = dsApp.GetActiveWorkspace();
            if (workspace == null)
            {
                return;
            }
            object[] menus = workspace.GetMenuItems() as object[];
            MenuItem menu = workspace.AddMenu(apiUuid, (menus == null ? 0 : menus.Length) + 1, MenuName);
            if (menu != null)
            {
                menu.InsertMenuItem(apiUuid, dsMenuItemType_e.dsMenuItemType_UserCommand, 1, "Add circle", userCommand.GetID());
            }
        }
        private void OnExecute()
        {
            Document dsDoc = dsApp.GetActiveDocument();
            if (dsDoc == null)
            {
                return;
            }
            CommandMessage message = dsApp.GetCommandMessage();
            MathPlane plane = dsApp.GetMathUtility().CreateXYPlane();
            double x;
            double y;
            double z;
            if (!message.PromptForPoint2("Center of the circle", false, 0, 0, 0, out x, out y, out z, plane))
            {
                return;
            }
            SketchManager sketch = dsDoc.GetModel().GetSketchManager();
            Circle circle = sketch.InsertCircle(x, y, z, 10.0);
            message.PrintLine(circle == null ? "Could not insert the circle." : "Circle added.");
        }
    }
}
