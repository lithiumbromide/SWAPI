---
title: "CreateEllipse Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateEllipse"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateEllipse.html"
---

# CreateEllipse Method (IMathUtility)

Creates a mathematical elliptical Arc defining an Ellipse using the specified parameters.

## Syntax

### Visual Basic

```vb
Function CreateEllipse( _
   ByVal Center As MathPoint, _
   ByVal MajorAxis As MathVector, _
   ByVal MinorAxis As MathVector, _
   ByVal MajorRadius As System.Double, _
   ByVal MinorRadius As System.Double _
) As MathEllipArc
```

### C#

```csharp
MathEllipArc CreateEllipse(
   MathPoint Center,
   MathVector MajorAxis,
   MathVector MinorAxis,
   System.double MajorRadius,
   System.double MinorRadius
)
```

### JScript

```
function CreateEllipse(
   Center : MathPoint,
   MajorAxis : MathVector,
   MinorAxis : MathVector,
   MajorRadius : System.double,
   MinorRadius : System.double
) : MathEllipArc;
```

### Managed Extensions for C++

```
MathEllipArc* CreateEllipse(
   MathPoint* Center,
   MathVector* MajorAxis,
   MathVector* MinorAxis,
   System.double MajorRadius,
   System.double MinorRadius
)
```

### C++/CLI

```cpp
MathEllipArc^ CreateEllipse(
   MathPoint^ Center,
   MathVector^ MajorAxis,
   MathVector^ MinorAxis,
   System.double MajorRadius,
   System.double MinorRadius
)
```

### Parameters

- `Center`: Center [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `MajorAxis`: Major [axis](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
- `MinorAxis`: Minor [axis](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
- `MajorRadius`: Major radius
- `MinorRadius`: Minor radius

### Return Value

[Mathematical elliptical Arc](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateEllipArc.html)

## Availability

DraftSight V1R5.0
