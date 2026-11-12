---
title: "Enabled Property (IContextMenuItem)"
project: ""
interface: "IContextMenuItem"
member: "Enabled"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~Enabled.html"
---

# Enabled Property (IContextMenuItem)

Gets or sets whether to enable this context-sensitive menu item.

## Syntax

### Visual Basic

```vb
Property Enabled As System.Boolean
```

### C#

```csharp
System.bool Enabled {get; set;}
```

### JScript

```
function get,set Enabled : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Enabled();
__property void set_Enabled(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Enabled {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to enable this context-sensitive menu item, false to not

## See Also

[IContextMenuItem Interface](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem.html)
[IContextMenuItem Members](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem_members.html)
[IContextMenuItem::GetMenuItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~GetMenuItems.html)
[IContextMenuItem::InsertMenuItem Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~InsertMenuItem.html)
[IApplication::AddCommandContextMenu Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddCommandContextMenu.html)
[IApplication::AddDefaultContextMenu Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddDefaultContextMenu.html)
[IApplication::AddObjectContextMenu Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddObjectContextMenu.html)
[IApplication::GetContextMenuItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetContextMenuItems.html)

## Availability

DraftSight V1R5.0
