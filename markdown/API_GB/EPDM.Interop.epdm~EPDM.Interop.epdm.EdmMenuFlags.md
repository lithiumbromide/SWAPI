---
title: "EdmMenuFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmMenuFlags"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.html"
---

# EdmMenuFlags Enumeration

Flags used by [IEdmCmdMgr5::AddCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.html) when writing an [add-in that supports menu commands](vbmenuitem.htm). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmMenuFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmMenuFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmMenuFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmMenu_Administration | 512 = The command is displayed in SOLIDWORKS PDM Professional Administration tool instead of the File Explorer |
| EdmMenu_ContextMenuItem | 1024 = The command is displayed in the file's context menu |
| EdmMenu_ContextMenuItemFolder | 2048 = The command is displayed in the folder's context menu |
| EdmMenu_HastItemToolbarButton | 8192 = The command has a button in the Item Explorer toolbar |
| EdmMenu_HasToolbarButton | 128 = The command has a button in the File Explorer toolbar; see IEdmCmdMgr5::AddToolbarImage |
| EdmMenu_ItemToolsMenu | 4096 = The command is displayed in the Item Explorer tools menu |
| EdmMenu_MustHaveSelection | 1 = The command is only available when the user has selected files or folders in the File Explorer file list |
| EdmMenu_NeverInContextMenu | 64 = The command should not be present in the right-click, context menu, only in the File Explorer Tools menu |
| EdmMenu_Nothing | 0 = Default behavior; no restrictions and no toolbar |
| EdmMenu_OnlyFiles | 2 = The command is not available for selections containing folders, only for files |
| EdmMenu_OnlyFolders | 4 = The command is not available for selections containing files, only for folders |
| EdmMenu_OnlyInContextMenu | 32 = The command should only be present in the right-click, context menu, not in the File Explorer Tools menu |
| EdmMenu_OnlyMultipleSelection | 16 = The command is only available for multiple selections, not for single files or folders |
| EdmMenu_OnlySingleSelection | 8 = The command is only available if only one file or folder has been selected, not for multiple selections |
| EdmMenu_OwnerDrawToolbarButton | 256 = The command uses custom drawing of its toolbar button by implementing IEdmAddInDrawButton5 |
| EdmMenu_ShowInMenuBarAction | 16384 = The command is displayed in the Action menu in the File Explorer toolbar |
| EdmMenu_ShowInMenuBarDisplay | 65536 = The command is displayed in the Display menu in the File Explorer toolbar |
| EdmMenu_ShowInMenuBarModify | 32768 = The command is displayed in the Modify menu in the File Explorer toolbar |
| EdmMenu_ShowInMenuBarTools | 131072 = The command is displayed in the Tools menu in the File Explorer toolbar |

## Remarks

The flags specify various properties for your command.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
