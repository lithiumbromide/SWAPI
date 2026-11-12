---
title: "Add-in Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/AddInApp.htm"
---

# Add-in Applications

Add-ins in SOLIDWORKS PDM Professional are:

- DLLs that implement the COM interface, [IEdmAddIn5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html).
- Added to a file vault through the [Add-in Properties dialog](AdminDlg.htm).
- Notified about SOLIDWORKS PDM Professional user actions:

  - [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) is called when the add-in is added to a file vault.
  - SOLIDWORKS PDM Professional calls [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) when a user performs an action that the add-in wants to be notified about, e.g., when a menu item is selected, a file is created, or a file is checked in or out.
- Programmed with hooks ([EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html)) into SOLIDWORKS PDM Professional. All hooks are handled through the IEdmAddIn5 interface.

The following samples show how to create a basic add-in written in:

- [VB.NET](DotNetAddIns.htm)
- [Visual C#](CSharpAddIns.htm)
- [Visual C++](cppaddin.htm)

After you create the basic add-in using the examples, see how to add hooks:

- Add a menu item and toolbar button in File Explorer using:

  - [VB.NET](vbmenuitem.htm)
  - [Visual C#](csharpmenuitem.htm)
  - [Visual C++](cppmenuitem.htm)
- Add hooks that get called when a file is checked in or out using:

  - [VB.NET](vbreactor.htm)
  - [Visual C#](csharpreactor.htm)
  - [Visual C++](cppreactor.htm)
- [Hook up a button in a file data card using VB.NET](vbcardbutton.htm)
- [Create serial numbers using an add-in written in VB.NET](vbserno.htm)
