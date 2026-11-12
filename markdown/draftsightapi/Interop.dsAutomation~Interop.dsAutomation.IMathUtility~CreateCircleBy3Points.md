---
title: "CreateCircleBy3Points Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateCircleBy3Points"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircleBy3Points.html"
---

# CreateCircleBy3Points Method (IMathUtility)

Creates a mathematical circular Arc defining a Circle using the specified three points.

## Syntax

### Visual Basic

```vb
Function CreateCircleBy3Points( _
   ByVal FirstPoint As MathPoint, _
   ByVal SecondPoint As MathPoint, _
   ByVal ThirdPoint As MathPoint _
) As MathCircArc
```

### C#

```csharp
MathCircArc CreateCircleBy3Points(
   MathPoint FirstPoint,
   MathPoint SecondPoint,
   MathPoint ThirdPoint
)
```

### JScript

```
function CreateCircleBy3Points(
   FirstPoint : MathPoint,
   SecondPoint : MathPoint,
   ThirdPoint : MathPoint
) : MathCircArc;
```

### Managed Extensions for C++

```
MathCircArc* CreateCircleBy3Points(
   MathPoint* FirstPoint,
   MathPoint* SecondPoint,
   MathPoint* ThirdPoint
)
```

### C++/CLI

```cpp
MathCircArc^ CreateCircleBy3Points(
   MathPoint^ FirstPoint,
   MathPoint^ SecondPoint,
   MathPoint^ ThirdPoint
)
```

### Parameters

- `FirstPoint`: First [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `SecondPoint`: Second [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `ThirdPoint`: Third [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

### Return Value

[Mathematical circular Arc](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircArc.html)
[IMathUtility::CreateCircArcBy3Points Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircArcBy3Points.html)
[IMathUtility::CreateCircle Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircle.html)

## Availability

DraftSight V1R6.0
