---
title: "AddCommandContextMenu Method (IApplication)"
project: ""
interface: "IApplication"
member: "AddCommandContextMenu"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~AddCommandContextMenu.html"
---

# AddCommandContextMenu Method (IApplication)

Adds a menu item to the specified command's context-sensitive menu.

## Syntax

### Visual Basic

```vb
Function AddCommandContextMenu( _
   ByVal ApiUuid As System.String, _
   ByVal ItemType As dsMenuItemType_e, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String, _
   ByVal CmdName As System.String _
) As ContextMenuItem
```

### C#

```csharp
ContextMenuItem AddCommandContextMenu(
   System.string ApiUuid,
   dsMenuItemType_e ItemType,
   System.string ItemName,
   System.string UserCmdID,
   System.string CmdName
)
```

### JScript

```
function AddCommandContextMenu(
   ApiUuid : System.String,
   ItemType : dsMenuItemType_e,
   ItemName : System.String,
   UserCmdID : System.String,
   CmdName : System.String
) : ContextMenuItem;
```

### Managed Extensions for C++

```
ContextMenuItem* AddCommandContextMenu(
   System.string* ApiUuid,
   dsMenuItemType_e ItemType,
   System.string* ItemName,
   System.string* UserCmdID,
   System.string* CmdName
)
```

### C++/CLI

```cpp
ContextMenuItem^ AddCommandContextMenu(
   System.String^ ApiUuid,
   dsMenuItemType_e ItemType,
   System.String^ ItemName,
   System.String^ UserCmdID,
   System.String^ CmdName
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `ItemType`: Type of menu item as defined in [dsMenuItemtype_e](Interop.dsAutomation~Interop.dsAutomation.dsMenuItemType_e.html)
- `ItemName`: Name of the menu item
- `UserCmdID`: User-defined command ID when ItemType is dsMenuItemType.dsMenuItemType_UserCommand
- `CmdName`: Name of the command with which to associate this context-sensitive menu item

### Return Value

[Context-sensitive menu item](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem.html) for CmdName

## Examples

[Create Context-sensitive Menu Items (C#)](Create_Context-sensitive_Menu_Items_Example_CSharp.htm)
[Create Context-sensitive Menu Items (VB.NET)](Create_Context-sensitive_Menu_Items_Example_VBNET.htm)
[Create Context-sensitive Menu Items (VBA)](Create_Context-sensitive_Menu_Items_Example_VBA.htm)

## Remarks

The context-sensitive menu appears when a user clicks the right-mouse button when the specified command is running.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AddDefaultContextMenu Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddDefaultContextMenu.html)
[IApplication::AddObjectContextMenu Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddObjectContextMenu.html)
[IApplication::GetContextMenuItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetContextMenuItems.html)
[IContextMenuItem::Remove Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Remove.html)
[IContextMenuItem::Enabled Property ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Enabled.html)

## Availability

DraftSight V1R5.0
