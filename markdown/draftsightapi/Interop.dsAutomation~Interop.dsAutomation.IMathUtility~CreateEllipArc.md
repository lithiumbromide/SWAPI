---
title: "CreateEllipArc Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateEllipArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateEllipArc.html"
---

# CreateEllipArc Method (IMathUtility)

Creates a mathematical elliptical Arc using the specified parameters.

## Syntax

### Visual Basic

```vb
Function CreateEllipArc( _
   ByVal Center As MathPoint, _
   ByVal MajorAxis As MathVector, _
   ByVal MinorAxis As MathVector, _
   ByVal MajorRadius As System.Double, _
   ByVal MinorRadius As System.Double, _
   ByVal StartAngle As System.Double, _
   ByVal EndAngle As System.Double _
) As MathEllipArc
```

### C#

```csharp
MathEllipArc CreateEllipArc(
   MathPoint Center,
   MathVector MajorAxis,
   MathVector MinorAxis,
   System.double MajorRadius,
   System.double MinorRadius,
   System.double StartAngle,
   System.double EndAngle
)
```

### JScript

```
function CreateEllipArc(
   Center : MathPoint,
   MajorAxis : MathVector,
   MinorAxis : MathVector,
   MajorRadius : System.double,
   MinorRadius : System.double,
   StartAngle : System.double,
   EndAngle : System.double
) : MathEllipArc;
```

### Managed Extensions for C++

```
MathEllipArc* CreateEllipArc(
   MathPoint* Center,
   MathVector* MajorAxis,
   MathVector* MinorAxis,
   System.double MajorRadius,
   System.double MinorRadius,
   System.double StartAngle,
   System.double EndAngle
)
```

### C++/CLI

```cpp
MathEllipArc^ CreateEllipArc(
   MathPoint^ Center,
   MathVector^ MajorAxis,
   MathVector^ MinorAxis,
   System.double MajorRadius,
   System.double MinorRadius,
   System.double StartAngle,
   System.double EndAngle
)
```

### Parameters

- `Center`: Center [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `MajorAxis`: Major [axis](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
- `MinorAxis`: Minor [axis](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
- `MajorRadius`: Major radius
- `MinorRadius`: Minor radius
- `StartAngle`: Start angle
- `EndAngle`: End angle

### Return Value

[Mathematical elliptical Arc](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)

## Examples

[Create and Transform Mathematical Elliptical Arc (C#)](Create_and_Transform_Mathematical_Elliptical_Arc_Example_CSharp.htm)
[Create and Transform Mathematical Elliptical Arc (VB.NET)](Create_and_Transform_Mathematical_Elliptical_Arc_Example_VBNET.htm)
[Create and Transform Mathematical Elliptical Arc (VBA)](Create_and_Transform_Mathematical_Elliptical_Arc_Example_VBA.htm)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateEllipse Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateEllipse.html)

## Availability

DraftSight V1R5.0
