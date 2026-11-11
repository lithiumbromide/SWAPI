---
title: "SetFrozenInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "SetFrozenInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~SetFrozenInViewport.html"
---

# SetFrozenInViewport Method (ILayer)

Sets whether this Layer is frozen or thawed in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub SetFrozenInViewport( _
   ByVal IsFrozen As System.Boolean, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void SetFrozenInViewport(
   System.bool IsFrozen,
   Viewport Viewport
)
```

### JScript

```
function SetFrozenInViewport(
   IsFrozen : System.boolean,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void SetFrozenInViewport(
   System.bool IsFrozen,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void SetFrozenInViewport(
   System.bool IsFrozen,
   Viewport^ Viewport
)
```

### Parameters

- `IsFrozen`: True if this Layer is frozen in the specified Viewport, false if this Layer is thawed in the specified Viewport
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetFrozenInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetFrozenInViewport.html)
[ILayer::FrozenInNewViewport Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~FrozenInNewViewport.html)
[ILayer::Frozen Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~Frozen.html)

## Availability

DraftSight V1R6.0
