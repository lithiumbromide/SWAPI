---
title: "Creating Add-in Hooks (VB.NET)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/vbreactor.htm"
---

# Creating Add-in Hooks (VB.NET)

This topic shows how to implement [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) and [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) in your add-in to have SOLIDWORKS PDM Professional notify your add-in whenever a file is added, checked out, or checked in.

**NOTE:** Because SOLIDWORKS PDM Professional cannot force a reload of add-ins if they are written in .NET, all client machines must be restarted to ensure that the latest version of the add-in is used.

1. Call [IEdmCmdMgr5::AddHook](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html) from your add-in's GetAddInInfo method for each activity you want your add-in to know about. Implement IEdmAddIn5::GetAddInInfo in your add-in as follows:
2. Implement IEdmAddIn5::OnCmd in your add-in as follows:
3. Click **Build > Build Solution** to build the add-in.
4. Install the add-in through the SOLIDWORKS PDM Professional Administration tool:

  1. Open the SOLIDWORKS PDM Professional Administration tool.
  2. Expand the vault where you want to install this add-in and log in as Admin.
  3. Right-click **Add-ins** and click **New Add-in**.
  4. Browse to `project_path``\``project_name\project_name`**\bin\Debug**, click `project_name`**.dll** and **EPDM.Interop.epdm.dll**.
  5. Click **Open**.
  6. Click **OK**.
  7. Click **OK**.
5. Try adding, checking out, and checking in vault files.

**NOTE:** OnCmd is not called during check-in if the file is not modified before it is checked in. During check-in of unmodified files, SOLIDWORKS PDM Professional triggers an "undo check-out" event. To handle this "undo check-out" event, add hooks for [EdmCmdType.EdmCmd_PreUndoLock](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html) and [EdmCmdType.EdmCmd_PostUndoLock](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html) to your add-in's GetAddInInfo.
