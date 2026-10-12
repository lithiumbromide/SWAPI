---
title: "CreateMenuFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "CreateMenuFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.CreateMenuFlags.html"
---

# CreateMenuFlags Enumeration

Types of menu used in calls to [IEdmVault5::CreatePluginMenu](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~CreatePluginMenu.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum CreateMenuFlags
   Inherits System.Enum
```

### C#

```csharp
public enum CreateMenuFlags : System.Enum
```

### C++/CLI

```cpp
public enum class CreateMenuFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Cmf_AddMenuIcons | 32 = Adds toolbar button bitmaps to the menu |
| Cmf_AllItemsInSameFolder | 1 = All of the selected files and folders are located in the same parent folder |
| Cmf_ContextMenu | 8 = Context-sensitive menu; not a standard popup menu |
| Cmf_ContextMenuItem | 64 = Context-sensitive menu for an item |
| Cmf_ContextMenuItemFolder | 128 = Context-sensitive menu for an item folder |
| Cmf_DisableAddInReload | 16 = Prevent SOLIDWORKS PDM Professional from querying the database to check whether updates have been made to the number of installed add-ins; this can be used to optimize the execution when called several times in a row |
| Cmf_GrayOutInvalidItems | 4 = Disable menu items that are not currently applicable |
| Cmf_IncludeAdminReactors | 2 = Include the Administrate Add-ins command |
| Cmf_ItemToolsMenu | 256 = Tools > Item menu in the Item Explorer |
| Cmf_MenuBarAction | 512 = Actions menu in the File Explorer |
| Cmf_MenuBarDisplay | 2048 = Display menu in File Explorer |
| Cmf_MenuBarModify | 1024 = Modify menu in File Explorer |
| Cmf_MenuBarTools | 4096 = Tools menu in File Explorer |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
