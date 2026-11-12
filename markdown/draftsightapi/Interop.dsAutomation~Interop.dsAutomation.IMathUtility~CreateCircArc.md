---
title: "CreateCircArc Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateCircArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircArc.html"
---

# CreateCircArc Method (IMathUtility)

Creates a mathematical circular Arc.

## Syntax

### Visual Basic

```vb
Function CreateCircArc( _
   ByVal Center As MathPoint, _
   ByVal Normal As MathVector, _
   ByVal RefVector As MathVector, _
   ByVal Radius As System.Double, _
   ByVal StartAngle As System.Double, _
   ByVal EndEngle As System.Double _
) As MathCircArc
```

### C#

```csharp
MathCircArc CreateCircArc(
   MathPoint Center,
   MathVector Normal,
   MathVector RefVector,
   System.double Radius,
   System.double StartAngle,
   System.double EndEngle
)
```

### JScript

```
function CreateCircArc(
   Center : MathPoint,
   Normal : MathVector,
   RefVector : MathVector,
   Radius : System.double,
   StartAngle : System.double,
   EndEngle : System.double
) : MathCircArc;
```

### Managed Extensions for C++

```
MathCircArc* CreateCircArc(
   MathPoint* Center,
   MathVector* Normal,
   MathVector* RefVector,
   System.double Radius,
   System.double StartAngle,
   System.double EndEngle
)
```

### C++/CLI

```cpp
MathCircArc^ CreateCircArc(
   MathPoint^ Center,
   MathVector^ Normal,
   MathVector^ RefVector,
   System.double Radius,
   System.double StartAngle,
   System.double EndEngle
)
```

### Parameters

- `Center`: Center [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of the mathematical circular Arc
- `Normal`: [Vector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html) normal to the plane of the mathematical circular Arc
- `RefVector`: Reference [vector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html) defining angle 0 of the mathematical circular Arc
- `Radius`: Radius of the mathematical circular Arc
- `StartAngle`: Start angle of the mathematical circular Arc
- `EndEngle`: End angle of the mathematical circular Arc

### Return Value

[Mathematical circular Arc](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)

## Examples

[Create Mathematical Circular Arcs (C#)](Create_Mathemetical_Circular_Arcs_Example_CSharp.htm)
[Create Mathematical Circular Arcs (VB.NET)](Create_Mathematical_Circular_Arcs_Example_VBNET.htm)
[Create Mathematical Circular Arcs (VBA)](Create_Mathematical_Circular_Arcs_Example_VBA.htm)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateCircArcBy3Points Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircArcBy3Points.html)
[IMathUtility::CreateCircle Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircle.html)
[IMathUtility::CreateCircleBy3Points Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircleBy3Points.html)

## Availability

DraftSight V1R5.0
