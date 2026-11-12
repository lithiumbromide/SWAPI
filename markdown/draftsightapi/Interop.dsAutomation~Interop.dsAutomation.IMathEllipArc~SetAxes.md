---
title: "SetAxes Method (IMathEllipArc)"
project: ""
interface: "IMathEllipArc"
member: "SetAxes"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~SetAxes.html"
---

# SetAxes Method (IMathEllipArc)

Sets the major and minor axes of this mathematical elliptical Arc.

## Syntax

### Visual Basic

```vb
Sub SetAxes( _
   ByVal MajorAxis As MathVector, _
   ByVal MinorAxis As MathVector _
)
```

### C#

```csharp
void SetAxes(
   MathVector MajorAxis,
   MathVector MinorAxis
)
```

### JScript

```
function SetAxes(
   MajorAxis : MathVector,
   MinorAxis : MathVector
);
```

### Managed Extensions for C++

```
void SetAxes(
   MathVector* MajorAxis,
   MathVector* MinorAxis
)
```

### C++/CLI

```cpp
void SetAxes(
   MathVector^ MajorAxis,
   MathVector^ MinorAxis
)
```

### Parameters

- `MajorAxis`: Major [axis](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html) of this mathematical elliptical Arc
- `MinorAxis`: Minor [axis](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html) of this mathematical elliptical Arc

## Examples

See the [IMathEllipArc](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html) examples.

## See Also

[IMathEllipArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)
[IMathEllipArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc_members.html)
[IMathEllipArc::GetMajorAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetMajorAxis.html)
[IMathEllipArc::GetMinorAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetMinorAxis.html)
[IMathEllipArc::GetNormal Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetNormal.html)

## Availability

DraftSight V1R5.0
