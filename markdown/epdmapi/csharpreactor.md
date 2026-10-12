---
title: "Creating Add-in Hooks (C#)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/csharpreactor.htm"
---

# Creating Add-in Hooks (C#)

This topic shows how to program an add-in to have SOLIDWORKS PDM Professional notify your add-in whenever a file is added, checked out, or checked in to a vault.

**NOTE:** Because SOLIDWORKS PDM Professional cannot force a reload of add-ins if they are written in .NET, all client machines must be restarted to ensure that the latest version of the add-in is used.

1. Follow [Creating Menu Commands (C#)](csharpmenuitem.htm) to create a basic add-in.
2. In your add-in's [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) implementation, call [IEdmCmdMgr5::AddHook](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html) for each SOLIDWORKS PDM Professional activity that you want your add-in to be notified about. Implement IEdmAddIn5::GetAddInInfo as follows:
3. Implement [IEdmAddIn5::](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html)[OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) as follows:
4. Click **Build > Build Solution** to build the add-in.
5. Install the add-in through the SOLIDWORKS PDM Professional Administration tool:

  1. Open the SOLIDWORKS PDM Professional Administration tool.
  2. Expand the vault where you want to install this add-in and log in as Admin.
  3. Right-click **Add-ins** and click **New Add-in**.
  4. Browse to `project_path``\``project_name\project_name`**\bin\Debug**, click `project_name`**.dll** and **EPDM.Interop.epdm.dll**.
  5. Click **Open**.
  6. Click **OK**.
  7. Click **OK**.
6. Add, check out, or check in one or more vault files. A message box displays with the files added, checked out, or checked in.

**NOTE:** OnCmd is not called during check-in if the file is not modified. During check-in of unmodified files, SOLIDWORKS PDM Professional triggers an "undo check-out" event. To handle this "undo check-out" event, register [EdmCmdType.EdmCmd_PreUndoLock](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html) and [EdmCmdType.EdmCmd_PostUndoLock](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html) hooks in your add-in's implementation of IEdmAddIn5::GetAddInInfo.
