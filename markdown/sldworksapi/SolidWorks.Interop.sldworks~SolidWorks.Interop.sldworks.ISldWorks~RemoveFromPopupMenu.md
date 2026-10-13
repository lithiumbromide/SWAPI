---
title: "RemoveFromPopupMenu Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveFromPopupMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.html"
---

# RemoveFromPopupMenu Method (ISldWorks)

Removes the specified menu item from one or all specified context-sensitive menus (also called shortcut menus and pop-up menus) for the specified document types.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveFromPopupMenu( _
   ByVal CommandID As System.Integer, _
   ByVal DocumentType As System.Integer, _
   ByVal SelectionType As System.Integer, _
   ByVal RemoveParentMenu As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim DocumentType As System.Integer
Dim SelectionType As System.Integer
Dim RemoveParentMenu As System.Boolean
Dim value As System.Boolean

value = instance.RemoveFromPopupMenu(CommandID, DocumentType, SelectionType, RemoveParentMenu)
```

### C#

```csharp
System.bool RemoveFromPopupMenu(
   System.int CommandID,
   System.int DocumentType,
   System.int SelectionType,
   System.bool RemoveParentMenu
)
```

### C++/CLI

```cpp
System.bool RemoveFromPopupMenu(
   System.int CommandID,
   System.int DocumentType,
   System.int SelectionType,
   System.bool RemoveParentMenu
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandID`: Command ID of the command to remove as defined by [swCommands_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.html)
- `DocumentType`: Document types in which to remove the command as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `SelectionType`: Context-sensitive menu from which to remove the command as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

  NOTE: Specifying swSelEVERYTHING will remove the command from all context-sensitive menus
- `RemoveParentMenu`: True to remove the specified command's any parent menus, false to not

## VBA Syntax

See [SldWorks::RemoveFromPopupMenu](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveFromPopupMenu.html).

## Examples

[Remove Menu commands, Menus, and Toolbar Buttons (VBA)](Remove_Menu_Commands_Menus_and_Toolbar_Buttons_Example_VB.htm)

## Remarks

The removal of the specified menu item takes affect the next time the context-sensitive menu is displayed.

To remove main frame menu commands and menus, use [ISldWorks::RemoveFromMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveFromMenu.html).

This method is not persistent across SOLIDWORKS Design sessions.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html)
[ISldWorks::AddMenuItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.html)
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.html)
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
