---
title: "GetLineWeightInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "GetLineWeightInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~GetLineWeightInViewport.html"
---

# GetLineWeightInViewport Method (ILayer)

Gets the type of LineWeight for this Layer in the specified Viewport and whether the LineWeight is overridden in that Viewport.

## Syntax

### Visual Basic

```vb
Function GetLineWeightInViewport( _
   ByVal Viewport As Viewport, _
   ByRef IsOverride As System.Boolean _
) As dsLineWeight_e
```

### C#

```csharp
dsLineWeight_e GetLineWeightInViewport(
   Viewport Viewport,
   out System.bool IsOverride
)
```

### JScript

```
function GetLineWeightInViewport(
   Viewport : Viewport,
   IsOverride : System.boolean
) : dsLineWeight_e;
```

### Managed Extensions for C++

```
dsLineWeight_e GetLineWeightInViewport(
   Viewport* Viewport,
   [PARAMFLAG::Out] System.bool IsOverride
)
```

### C++/CLI

```cpp
dsLineWeight_e GetLineWeightInViewport(
   Viewport^ Viewport,
   [Out] System.bool IsOverride
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
- `IsOverride`: True if the LineWeight for this Layer is overridden in the specified Viewport, false if not

### Return Value

LineWeight as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::SetLineWeightInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetLineWeightInViewport.html)
[ILayer::RemoveLineWeightOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverride.html)
[ILayer::RemoveLineWeightOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverrides.html)
[ILayer::LineWeight Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~LineWeight.html)

## Availability

DraftSight V1R6.0
