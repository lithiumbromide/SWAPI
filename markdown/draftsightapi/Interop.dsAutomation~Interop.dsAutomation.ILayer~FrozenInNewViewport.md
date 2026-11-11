---
title: "FrozenInNewViewport Property (ILayer)"
project: ""
interface: "ILayer"
member: "FrozenInNewViewport"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~FrozenInNewViewport.html"
---

# FrozenInNewViewport Property (ILayer)

Gets or sets whether this Layer is frozen or thawed in newly created [Viewports](Interop.dsAutomation~Interop.dsAutomation.IViewport.html).

## Syntax

### Visual Basic

```vb
Property FrozenInNewViewport As System.Boolean
```

### C#

```csharp
System.bool FrozenInNewViewport {get; set;}
```

### JScript

```
function get,set FrozenInNewViewport : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_FrozenInNewViewport();
__property void set_FrozenInNewViewport(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool FrozenInNewViewport {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if this Layer if frozen in newly created Viewports, false if this Layer is thawed in newly created Viewports

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::Frozen Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~Frozen.html)
[ILayer::GetFrozenInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetFrozenInViewport.html)
[ILayer::SetFrozenInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetFrozenInViewport.html)

## Availability

DraftSight V1R6.0
