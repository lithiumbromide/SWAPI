---
title: "CreateCircArcBy3Points Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateCircArcBy3Points"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircArcBy3Points.html"
---

# CreateCircArcBy3Points Method (IMathUtility)

Creates a mathematical circular Arc through the specified start, through, and end points.

## Syntax

### Visual Basic

```vb
Function CreateCircArcBy3Points( _
   ByVal StartPoint As MathPoint, _
   ByVal ThroughPoint As MathPoint, _
   ByVal EndPoint As MathPoint _
) As MathCircArc
```

### C#

```csharp
MathCircArc CreateCircArcBy3Points(
   MathPoint StartPoint,
   MathPoint ThroughPoint,
   MathPoint EndPoint
)
```

### JScript

```
function CreateCircArcBy3Points(
   StartPoint : MathPoint,
   ThroughPoint : MathPoint,
   EndPoint : MathPoint
) : MathCircArc;
```

### Managed Extensions for C++

```
MathCircArc* CreateCircArcBy3Points(
   MathPoint* StartPoint,
   MathPoint* ThroughPoint,
   MathPoint* EndPoint
)
```

### C++/CLI

```cpp
MathCircArc^ CreateCircArcBy3Points(
   MathPoint^ StartPoint,
   MathPoint^ ThroughPoint,
   MathPoint^ EndPoint
)
```

### Parameters

- `StartPoint`: Start [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `ThroughPoint`: Through [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `EndPoint`: End [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

### Return Value

[Mathematical circular Arc](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircArc.html)
[IMathUtility::CreateCircle Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircle.html)
[IMathUtility::CreateCircleBy3Points Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircleBy3Points.html)

## Availability

DraftSight V1R5.0
