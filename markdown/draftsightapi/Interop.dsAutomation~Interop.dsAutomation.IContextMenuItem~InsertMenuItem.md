---
title: "InsertMenuItem Method (IContextMenuItem)"
project: ""
interface: "IContextMenuItem"
member: "InsertMenuItem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~InsertMenuItem.html"
---

# InsertMenuItem Method (IContextMenuItem)

Inserts a context-sensitive menu item for this context-sensitive menu item.

## Syntax

### Visual Basic

```vb
Function InsertMenuItem( _
   ByVal ApiUuid As System.String, _
   ByVal ItemType As dsMenuItemType_e, _
   ByVal Position As System.Integer, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String _
) As ContextMenuItem
```

### C#

```csharp
ContextMenuItem InsertMenuItem(
   System.string ApiUuid,
   dsMenuItemType_e ItemType,
   System.int Position,
   System.string ItemName,
   System.string UserCmdID
)
```

### JScript

```
function InsertMenuItem(
   ApiUuid : System.String,
   ItemType : dsMenuItemType_e,
   Position : System.int,
   ItemName : System.String,
   UserCmdID : System.String
) : ContextMenuItem;
```

### Managed Extensions for C++

```
ContextMenuItem* InsertMenuItem(
   System.string* ApiUuid,
   dsMenuItemType_e ItemType,
   System.int Position,
   System.string* ItemName,
   System.string* UserCmdID
)
```

### C++/CLI

```cpp
ContextMenuItem^ InsertMenuItem(
   System.String^ ApiUuid,
   dsMenuItemType_e ItemType,
   System.int Position,
   System.String^ ItemName,
   System.String^ UserCmdID
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `ItemType`: Type of context-sensitive menu item to insert as defined in [dsMenuItemType_e](Interop.dsAutomation~Interop.dsAutomation.dsMenuItemType_e.html)
- `Position`: 1-based index indicating where to insert the context-sensitive menu item
- `ItemName`: Name of the context-sensitive menu item
- `UserCmdID`: User-defined command ID when ItemType is dsMenuItemType_e.dsMenuItemType_UserCommand

### Return Value

[Context-sensitive menu item](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem.html)

## See Also

[IContextMenuItem Interface](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem.html)
[IContextMenuItem Members](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem_members.html)
[IContextMenuItem::GetMenuItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~GetMenuItems.html)
[IContextMenuItem::Remove Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Remove.html)
[IContextMenuItem::Enabled Property ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Enabled.html)

## Availability

DraftSight V1R5.0
