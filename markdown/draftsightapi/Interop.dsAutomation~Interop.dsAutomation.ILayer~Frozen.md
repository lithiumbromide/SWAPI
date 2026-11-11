---
title: "Frozen Property (ILayer)"
project: ""
interface: "ILayer"
member: "Frozen"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~Frozen.html"
---

# Frozen Property (ILayer)

Gets or sets whether the Layer is frozen or thawed.

## Syntax

### Visual Basic

```vb
Property Frozen As System.Boolean
```

### C#

```csharp
System.bool Frozen {get; set;}
```

### JScript

```
function get,set Frozen : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Frozen();
__property void set_Frozen(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Frozen {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the Layer is frozen, false if the Layer is thawed

## Remarks

Freezing and thawing a layer controls the visibility and the ability to edit the Layer.

When a Layer is frozen, its entities are protected and not visible. Unlike entities on Layers that are turned off, entities on frozen Layers are ignored when the drawing rebuilds. Entities on thawed Layers are unprotected and visible.

You cannot freeze the active layer.

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::Shown Property](Interop.dsAutomation~Interop.dsAutomation.ILayer~Shown.html)
[ILayer::GetFrozenInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetFrozenInViewport.html)
[ILayer::SetFrozenInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetFrozenInViewport.html)

## Availability

DraftSight V1R1.1
