---
title: "SetTranparencyInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "SetTranparencyInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~SetTranparencyInViewport.html"
---

# SetTranparencyInViewport Method (ILayer)

Sets the [transparency](Interop.dsAutomation~Interop.dsAutomation.ITransparency.html) percentage for this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub SetTranparencyInViewport( _
   ByVal Transparency As System.Integer, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void SetTranparencyInViewport(
   System.int Transparency,
   Viewport Viewport
)
```

### JScript

```
function SetTranparencyInViewport(
   Transparency : System.int,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void SetTranparencyInViewport(
   System.int Transparency,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void SetTranparencyInViewport(
   System.int Transparency,
   Viewport^ Viewport
)
```

### Parameters

- `Transparency`: Transparency percentage, which must between 0 and 90 where 0 means no transparency (opaque)
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetTranparencyInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetTranparencyInViewport.html)
[ILayer::RemoveTransparencyOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverride.html)
[ILayer::RemoveTransparencyOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverrides.html)
[ILayer::Transparency Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~Transparency.html)

## Availability

DraftSight V1R6.0
