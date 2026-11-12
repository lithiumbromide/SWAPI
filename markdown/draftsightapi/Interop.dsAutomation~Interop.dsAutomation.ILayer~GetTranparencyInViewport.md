---
title: "GetTranparencyInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "GetTranparencyInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~GetTranparencyInViewport.html"
---

# GetTranparencyInViewport Method (ILayer)

Gets the [transparency](Interop.dsAutomation~Interop.dsAutomation.ITransparency.html) percentage for this Layer in the specified Viewport and gets whether the transparency in this Layer is overridden in that Viewport.

## Syntax

### Visual Basic

```vb
Function GetTranparencyInViewport( _
   ByVal Viewport As Viewport, _
   ByRef IsOverride As System.Boolean _
) As System.Integer
```

### C#

```csharp
System.int GetTranparencyInViewport(
   Viewport Viewport,
   out System.bool IsOverride
)
```

### JScript

```
function GetTranparencyInViewport(
   Viewport : Viewport,
   IsOverride : System.boolean
) : System.int;
```

### Managed Extensions for C++

```
System.int GetTranparencyInViewport(
   Viewport* Viewport,
   [PARAMFLAG::Out] System.bool IsOverride
)
```

### C++/CLI

```cpp
System.int GetTranparencyInViewport(
   Viewport^ Viewport,
   [Out] System.bool IsOverride
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
- `IsOverride`: True if transparency in this Layer is overridden in the specified Viewport, false if not

### Return Value

Transparency percentage (see **Remarks**)

## Remarks

The transparency percentage is between 0 and 90 where 0 means no transparency (opaque).

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::RemoveTransparencyOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverride.html)
[ILayer::RemoveTransparencyOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverrides.html)
[ILayer::SetTranparencyInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetTranparencyInViewport.html)
[ILayer::Transparency Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~Transparency.html)

## Availability

DraftSight V1R6.0
