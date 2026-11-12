---
title: "GetContextMenuItems Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetContextMenuItems"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetContextMenuItems.html"
---

# GetContextMenuItems Method (IApplication)

Gets the top-level context-sensitive menu items added by [IApplication::AddCommandContextMenu](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddCommandContextMenu.html), [IApplication::AddDefaultContextMenu](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddDefaultContextMenu.html), and [IApplication::AddObjectContextMenu](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddObjectContextMenu.html).

## Syntax

### Visual Basic

```vb
Function GetContextMenuItems() As System.Object
```

### C#

```csharp
System.object GetContextMenuItems()
```

### JScript

```
function GetContextMenuItems() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetContextMenuItems();
```

### C++/CLI

```cpp
System.Object^ GetContextMenuItems();
```

### Return Value

Array of [context-sensitive menu items](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem.html)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IContextMenuItem::Remove Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Remove.html)
[IContextMenuItem::GetMenuItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~GetMenuItems.html)
[IContextMenuItem::Enabled Property ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Enabled.html)

## Availability

DraftSight V1R5.0
