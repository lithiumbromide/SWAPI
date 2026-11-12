---
title: "Creating Add-in Hooks (C++)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/cppreactor.htm"
---

# Creating Add-in Hooks (C++)

This topic shows how to implement [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) and [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) in your add-in to have SOLIDWORKS PDM Professional notify your add-in whenever a file is added, checked out, or checked in.

1. Call [IEdmCmdMgr5::AddHook](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html) from your add-in's GetAddInInfo method for each activity you want your add-in to know about. Implement IEdmAddIn5::GetAddInInfo in your add-in as follows:
2. Implement IEdmAddIn5::OnCmd in your add-in as follows:
3. Build the add-in DLL and add it to the file vault using the [Administration tool](AdminDlg.htm).
4. Try adding, checking out, and checking in vault files.

**NOTE:** OnCmd is not called during check-in if the file is not modified before it is checked in. During check-in of unmodified files, SOLIDWORKS PDM Professional triggers an "undo check-out" event. To handle this "undo check-out" event, add hooks for [EdmCmdType.EdmCmd_PreUndoLock](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html) and [EdmCmdType.EdmCmd_PostUndoLock](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html) to your add-in's GetAddInInfo.

### See Also

[Creating Add-ins (C++)](cppaddin.htm)

[Creating Add-in Hooks (VB.NET)](vbreactor.htm)
