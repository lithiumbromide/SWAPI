---
title: "OnMenuItem2 Method (IEdmMenu7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMenu7"
member: "OnMenuItem2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu7~OnMenuItem2.html"
---

# OnMenuItem2 Method (IEdmMenu7)

Executes the command for the selected menu item.

## Syntax

### Visual Basic

```vb
Function OnMenuItem2( _
   ByVal lItemID As System.Integer, _
   ByVal lParentWnd As System.Integer, _
   ByVal lCurrentFolderID As System.Integer, _
   ByVal poSelObjects As IEdmSelectionList6 _
) As System.Integer
```

### C#

```csharp
System.int OnMenuItem2(
   System.int lItemID,
   System.int lParentWnd,
   System.int lCurrentFolderID,
   IEdmSelectionList6 poSelObjects
)
```

### C++/CLI

```cpp
System.int OnMenuItem2(
   System.int lItemID,
   System.int lParentWnd,
   System.int lCurrentFolderID,
   IEdmSelectionList6^ poSelObjects
)
```

### Parameters

- `lItemID`: ID of the selected menu item
- `lParentWnd`: Parent window handle (HWND)
- `lCurrentFolderID`: ID of currently active folder
- `poSelObjects`: [List of selected objects](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6.html) (files, folders, items, etc.)

### Return Value

User-interface elements that should be refreshed as defined in [EdmRefreshFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefreshFlag.html)

## Examples

[Display Menu of Commands (VB.NET)](Display_Menu_of_Commands_Example_VBNET.htm)

## Remarks

You should call this method when a user selects a menu item belonging to this menu.

**NOTE:** This method supersedes IEdmMenu5::OnMenuItem, which only works with files and folders. IEdmMenu7::OnMenuItem2 works with files and folders as well as other object types such as items.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: Menu item does not belong to this menu.
- S_EDM_MENU_ITEM_NOT_APPLICABLE: The current selection of objects do not satisfy the constraints set by the command author. See [EdmMenuFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.html) sent to [IEdmCmdMgr5::AddCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.html).

## See Also

[IEdmMenu7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu7.html)
[IEdmMenu7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu7_members.html)

## Availability

SOLIDWORKS PDM Professional 2011
