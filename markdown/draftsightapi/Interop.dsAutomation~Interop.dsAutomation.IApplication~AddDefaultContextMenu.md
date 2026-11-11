---
title: "AddDefaultContextMenu Method (IApplication)"
project: ""
interface: "IApplication"
member: "AddDefaultContextMenu"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~AddDefaultContextMenu.html"
---

# AddDefaultContextMenu Method (IApplication)

Adds a menu item to the DraftSight default context-sensitive menu.

## Syntax

### Visual Basic

```vb
Function AddDefaultContextMenu( _
   ByVal ApiUuid As System.String, _
   ByVal ItemType As dsMenuItemType_e, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String _
) As ContextMenuItem
```

### C#

```csharp
ContextMenuItem AddDefaultContextMenu(
   System.string ApiUuid,
   dsMenuItemType_e ItemType,
   System.string ItemName,
   System.string UserCmdID
)
```

### JScript

```
function AddDefaultContextMenu(
   ApiUuid : System.String,
   ItemType : dsMenuItemType_e,
   ItemName : System.String,
   UserCmdID : System.String
) : ContextMenuItem;
```

### Managed Extensions for C++

```
ContextMenuItem* AddDefaultContextMenu(
   System.string* ApiUuid,
   dsMenuItemType_e ItemType,
   System.string* ItemName,
   System.string* UserCmdID
)
```

### C++/CLI

```cpp
ContextMenuItem^ AddDefaultContextMenu(
   System.String^ ApiUuid,
   dsMenuItemType_e ItemType,
   System.String^ ItemName,
   System.String^ UserCmdID
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `ItemType`: Type of menu item as defined in [dsMenuItemType_e](Interop.dsAutomation~Interop.dsAutomation.dsMenuItemType_e.html)
- `ItemName`: Name of the menu item
- `UserCmdID`: User-defined command ID when ItemType is dsMenuItemType_e.dsMenuItemType_UserCommand

### Return Value

[Context-sensitive menu item](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem.html) for DraftSight

## Examples

[Create Context-sensitive Menu Items (C#)](Create_Context-sensitive_Menu_Items_Example_CSharp.htm)
[Create Context-sensitive Menu Items (VB.NET)](Create_Context-sensitive_Menu_Items_Example_VBNET.htm)
[Create Context-sensitive Menu Items (VBA)](Create_Context-sensitive_Menu_Items_Example_VBA.htm)

## Remarks

The DraftSight context-sensitive menu appears if a user presses the right-mouse button when:

- the cursor is anywhere in a drawing,
- an entity is not selected, and
- a command is not running.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AddCommandContextMenu Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddCommandContextMenu.html)
[IApplication::AddObjectContextMenu Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddObjectContextMenu.html)
[IApplication::GetContextMenuItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetContextMenuItems.html)
[IContextMenuItem::Remove Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Remove.html)
[IContextMenuItem::Enabled Property ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Enabled.html)

## Availability

DraftSight V1R5.0
