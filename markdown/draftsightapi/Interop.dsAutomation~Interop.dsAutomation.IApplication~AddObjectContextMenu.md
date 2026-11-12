---
title: "AddObjectContextMenu Method (IApplication)"
project: ""
interface: "IApplication"
member: "AddObjectContextMenu"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~AddObjectContextMenu.html"
---

# AddObjectContextMenu Method (IApplication)

Adds a menu item to the specified object type's context-sensitive menu.

## Syntax

### Visual Basic

```vb
Function AddObjectContextMenu( _
   ByVal ApiUuid As System.String, _
   ByVal ItemType As dsMenuItemType_e, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String, _
   ByVal ObjectType As dsObjectType_e _
) As ContextMenuItem
```

### C#

```csharp
ContextMenuItem AddObjectContextMenu(
   System.string ApiUuid,
   dsMenuItemType_e ItemType,
   System.string ItemName,
   System.string UserCmdID,
   dsObjectType_e ObjectType
)
```

### JScript

```
function AddObjectContextMenu(
   ApiUuid : System.String,
   ItemType : dsMenuItemType_e,
   ItemName : System.String,
   UserCmdID : System.String,
   ObjectType : dsObjectType_e
) : ContextMenuItem;
```

### Managed Extensions for C++

```
ContextMenuItem* AddObjectContextMenu(
   System.string* ApiUuid,
   dsMenuItemType_e ItemType,
   System.string* ItemName,
   System.string* UserCmdID,
   dsObjectType_e ObjectType
)
```

### C++/CLI

```cpp
ContextMenuItem^ AddObjectContextMenu(
   System.String^ ApiUuid,
   dsMenuItemType_e ItemType,
   System.String^ ItemName,
   System.String^ UserCmdID,
   dsObjectType_e ObjectType
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `ItemType`: Type of menu item as defined in [dsMenuItemType_e](Interop.dsAutomation~Interop.dsAutomation.dsMenuItemType_e.html)
- `ItemName`: Name of the menu item
- `UserCmdID`: User-defined command ID when ItemType is dsMenuItemType_e.dsMenuItemType_UserCommand
- `ObjectType`: Type of object with which to associate this context-sensitive menu item as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)

### Return Value

[Context-sensitive menu](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem.html) for ObjectType

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AddCommandContextMenu Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddCommandContextMenu.html)
[IApplication::AddDefaultContextMenu Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddDefaultContextMenu.html)
[IApplication::GetContextMenuItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetContextMenuItems.html)
[IContextMenuItem::Remove Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Remove.html)
[IContextMenuItem::Enabled Property ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Enabled.html)

## Availability

DraftSight V1R5.0
