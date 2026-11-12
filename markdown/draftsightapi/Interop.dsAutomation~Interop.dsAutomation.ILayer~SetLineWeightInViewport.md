---
title: "SetLineWeightInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "SetLineWeightInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~SetLineWeightInViewport.html"
---

# SetLineWeightInViewport Method (ILayer)

Sets the type of LineWeight for this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub SetLineWeightInViewport( _
   ByVal LineWeight As dsLineWeight_e, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void SetLineWeightInViewport(
   dsLineWeight_e LineWeight,
   Viewport Viewport
)
```

### JScript

```
function SetLineWeightInViewport(
   LineWeight : dsLineWeight_e,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void SetLineWeightInViewport(
   dsLineWeight_e LineWeight,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void SetLineWeightInViewport(
   dsLineWeight_e LineWeight,
   Viewport^ Viewport
)
```

### Parameters

- `LineWeight`: LineWeight as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetLineWeightInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetLineWeightInViewport.html)
[ILayer::LineWeight Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~LineWeight.html)

## Availability

DraftSight V1R6.0
