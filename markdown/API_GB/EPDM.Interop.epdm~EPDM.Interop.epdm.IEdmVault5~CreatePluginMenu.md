---
title: "CreatePluginMenu Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "CreatePluginMenu"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~CreatePluginMenu.html"
---

# CreatePluginMenu Method (IEdmVault5)

Obsolete. Superseded by [IEdmVault12::CreatePluginMenu2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault12~CreatePluginMenu2.html).

## Syntax

### Visual Basic

```vb
Function CreatePluginMenu( _
   ByVal hMenu As System.Integer, _
   ByVal lInsertPosition As System.Integer, _
   ByRef plStartID As System.Integer, _
   ByVal lSelFileCount As System.Integer, _
   ByVal lSelFolderCount As System.Integer, _
   ByVal lCreateMenuFlags As System.Integer, _
   ByRef plItemCount As System.Integer _
) As IEdmMenu5
```

### C#

```csharp
IEdmMenu5 CreatePluginMenu(
   System.int hMenu,
   System.int lInsertPosition,
   out System.int plStartID,
   System.int lSelFileCount,
   System.int lSelFolderCount,
   System.int lCreateMenuFlags,
   out System.int plItemCount
)
```

### C++/CLI

```cpp
IEdmMenu5^ CreatePluginMenu(
   System.int hMenu,
   System.int lInsertPosition,
   [Out] System.int plStartID,
   System.int lSelFileCount,
   System.int lSelFolderCount,
   System.int lCreateMenuFlags,
   [Out] System.int plItemCount
)
```

### Parameters

- `hMenu`: Handle of menu in which to insert add-in commands
- `lInsertPosition`: Zero-based index of the position in the menu where new menu items should be inserted; -1 to append new menu items to the bottom of the menu
- `plStartID`: Next available menu command ID (see **Remarks**)
- `lSelFileCount`: Number of selected files
- `lSelFolderCount`: Number of selected folders
- `lCreateMenuFlags`: Combination of [CreateMenuFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.CreateMenuFlags.html) bits
- `plItemCount`: Number of menu items added

### Return Value

[IEdmMenu5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5.html) (see **Remarks**)

## Examples

## Remarks

When this method is called, plStartID should be the first free menu command ID that a new command is assigned. When this method returns, plStartID is the first free menu command ID after IDs for new menu commands have been reserved.

When the user chooses one of the menu items added by this method, your program must call [IEdmMenu5::OnMenuItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~OnMenuItem.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
