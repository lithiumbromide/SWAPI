---
title: "AddCmd Method (IEdmCmdMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCmdMgr5"
member: "AddCmd"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.html"
---

# AddCmd Method (IEdmCmdMgr5)

Adds a toolbar button to the File Explorer **Tools** menu and a menu command to the right-click context-sensitive menu of SOLIDWORKS PDM Professional vault files and folders.

## Syntax

### Visual Basic

```vb
Sub AddCmd( _
   ByVal lCmdID As System.Integer, _
   ByVal bsMenuString As System.String, _
   Optional ByVal lEdmMenuFlags As System.Integer, _
   Optional ByVal bsStatusBarHelp As System.String, _
   Optional ByVal bsToolbarToolTip As System.String, _
   Optional ByVal lToolbarButtonIndex As System.Integer, _
   Optional ByVal lToolbarImageID As System.Integer _
)
```

### C#

```csharp
void AddCmd(
   System.int lCmdID,
   System.string bsMenuString,
   System.int lEdmMenuFlags,
   System.string bsStatusBarHelp,
   System.string bsToolbarToolTip,
   System.int lToolbarButtonIndex,
   System.int lToolbarImageID
)
```

### C++/CLI

```cpp
void AddCmd(
   System.int lCmdID,
   System.String^ bsMenuString,
   System.int lEdmMenuFlags,
   System.String^ bsStatusBarHelp,
   System.String^ bsToolbarToolTip,
   System.int lToolbarButtonIndex,
   System.int lToolbarImageID
)
```

### Parameters

- `lCmdID`: Command ID (see **Remarks**)
- `bsMenuString`: Text to show in the menu
- `lEdmMenuFlags`: Optional combination of [EdmMenuFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.html)
- `bsStatusBarHelp`: Optional text to show in the File Explorer status bar when the user highlights the menu entry in the right-click context menu
- `bsToolbarToolTip`: Optional message to display when the cursor is located over the command's toolbar button
- `lToolbarButtonIndex`: Optional index of a toolbar button in a resource image (see **Remarks**)
- `lToolbarImageID`: Optional ID of the image to use as a toolbar button (see **Remarks**)

## Remarks

Call this method in your implementation of [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) to:

- Add command buttons to the File Explorer toolbar. Before calling IEdmCmdMgr5::AddCmd, call [IEdmCmdMgr5::AddToolbarImage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddToolbarImage.html) to register an image with the toolbar button you want to add.
- Add menu commands to the File Explorer Tools menu.
- Add menu commands to the right-click context menu of files or folders in the SOLIDWORKS PDM Professional vault.

lCmdID can be any value. SOLIDWORKS PDM Professional passes it to your implementation of [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) via [EdmCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)::mlCmdID.

lToolbarButtonIndex is the index of the toolbar image in a resource image that contains several images.

lToolbarImageID is the same as the lImageID parameter of IEdmCmdMgr5::AddToolbarImage.

**NOTE:** Menu commands and toolbar buttons added using this method display only when the user browses a SOLIDWORKS PDM Professional file vault. They do not display for ordinary Windows folders.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCmdMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5.html)
[IEdmCmdMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5_members.html)
[Administration Menu for Add-ins](AddInAdminMenu.htm)
[Creating Menu Commands (VB.NET)](vbmenuitem.htm)

## Availability

SOLIDWORKS PDM Professional Version 5.2
