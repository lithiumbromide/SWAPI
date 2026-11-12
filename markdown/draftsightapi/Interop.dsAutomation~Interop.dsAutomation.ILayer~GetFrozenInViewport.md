---
title: "GetFrozenInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "GetFrozenInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~GetFrozenInViewport.html"
---

# GetFrozenInViewport Method (ILayer)

Gets whether this Layer is frozen or thawed in the specified Viewport.

## Syntax

### Visual Basic

```vb
Function GetFrozenInViewport( _
   ByVal Viewport As Viewport _
) As System.Boolean
```

### C#

```csharp
System.bool GetFrozenInViewport(
   Viewport Viewport
)
```

### JScript

```
function GetFrozenInViewport(
   Viewport : Viewport
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetFrozenInViewport(
   Viewport* Viewport
)
```

### C++/CLI

```cpp
System.bool GetFrozenInViewport(
   Viewport^ Viewport
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

### Return Value

True if this Layer is frozen in the specified Viewport, false if this Layer is thawed in the specified Viewport

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::SetFrozenInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetFrozenInViewport.html)
[ILayer::FrozenInNewViewport Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~FrozenInNewViewport.html)
[ILayer::Frozen Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~Frozen.html)

## Availability

DraftSight V1R6.0
