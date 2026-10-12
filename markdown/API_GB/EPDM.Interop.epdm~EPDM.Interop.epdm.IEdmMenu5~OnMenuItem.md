---
title: "OnMenuItem Method (IEdmMenu5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMenu5"
member: "OnMenuItem"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~OnMenuItem.html"
---

# OnMenuItem Method (IEdmMenu5)

Obsolete. Superseded by [IEdmMenu7::OnMenuItem2.](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu7~OnMenuItem2.html)

## Syntax

### Visual Basic

```vb
Function OnMenuItem( _
   ByVal lItemID As System.Integer, _
   ByVal lParentWnd As System.Integer, _
   ByVal lCurrentFolderID As System.Integer, _
   ByVal poSelFiles As EdmSelectionList5, _
   ByVal poSelFolders As EdmSelectionList5 _
) As System.Integer
```

### C#

```csharp
System.int OnMenuItem(
   System.int lItemID,
   System.int lParentWnd,
   System.int lCurrentFolderID,
   EdmSelectionList5 poSelFiles,
   EdmSelectionList5 poSelFolders
)
```

### C++/CLI

```cpp
System.int OnMenuItem(
   System.int lItemID,
   System.int lParentWnd,
   System.int lCurrentFolderID,
   EdmSelectionList5^ poSelFiles,
   EdmSelectionList5^ poSelFolders
)
```

### Parameters

- `lItemID`: ID of the selected menu item
- `lParentWnd`: Parent window handle (HWND)
- `lCurrentFolderID`: ID of the currently active folder
- `poSelFiles`: [List of selected files](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html)
- `poSelFolders`: [List of selected folders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html)

### Return Value

User-interface elements that should be refreshed as defined in [EdmRefreshFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefreshFlag.html)

## Remarks

You should call this method when a user selects a menu item belonging to this menu.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: Menu item does not belong to this menu.
- S_EDM_MENU_ITEM_NOT_APPLICABLE: The current selection of files and folders do not satisfy the constraints set by the command author. See [EdmMenuFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.html) sent to [IEdmCmdMgr5::AddCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.html).

## See Also

[IEdmMenu5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5.html)
[IEdmMenu5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
