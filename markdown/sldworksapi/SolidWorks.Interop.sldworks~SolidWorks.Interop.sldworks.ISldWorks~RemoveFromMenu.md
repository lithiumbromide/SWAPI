---
title: "RemoveFromMenu Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveFromMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.html"
---

# RemoveFromMenu Method (ISldWorks)

Removes:

- the specified command from all main frame menus or a toolbar or both
- the specified command's parent menus

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveFromMenu( _
   ByVal CommandID As System.Integer, _
   ByVal DocumentType As System.Integer, _
   ByVal Option As System.Integer, _
   ByVal RemoveParentMenu As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim DocumentType As System.Integer
Dim Option As System.Integer
Dim RemoveParentMenu As System.Boolean
Dim value As System.Boolean

value = instance.RemoveFromMenu(CommandID, DocumentType, Option, RemoveParentMenu)
```

### C#

```csharp
System.bool RemoveFromMenu(
   System.int CommandID,
   System.int DocumentType,
   System.int Option,
   System.bool RemoveParentMenu
)
```

### C++/CLI

```cpp
System.bool RemoveFromMenu(
   System.int CommandID,
   System.int DocumentType,
   System.int Option,
   System.bool RemoveParentMenu
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandID`: Command ID of the command to remove as defined by [swCommands_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.html)
- `DocumentType`: Document types in which to remove the command as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `Option`: - 1 = Menu
  - 2 = Toolbar
  - 3 = Both menu and toolbar
- `RemoveParentMenu`: True to remove the specified command's parent menu, false to not

  NOTE: This parameter is specific to menus only; it does not affect toolbars.

### Return Value

True if the specified items are removed, false if not

## VBA Syntax

See [SldWorks::RemoveFromMenu](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveFromMenu.html).

## Examples

[Remove Menu Commands, Menus, and Toolbar Buttons (VBA)](Remove_Menu_Commands_Menus_and_Toolbar_Buttons_Example_VB.htm)

## Remarks

This method does not affect context-sensitive menus (also called shortcut menus and pop-up menus); this command only affects main frame menus and toolbars. To remove commands and parent menus from context-sensitive menus, use [ISldWorks::RemoveFromPopupMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.html).

The specified items are removed after this method executes, and their removal can be seen immediately.

This method is not persistent across SOLIDWORKS Design sessions.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html)
[ISldWorks::AddMenuItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.html)
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html)
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
