---
title: "CreateCircle Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreateCircle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircle.html"
---

# CreateCircle Method (IMathUtility)

Creates a mathematical circular Arc defining a Circle with the specified center, normal, and radius.

## Syntax

### Visual Basic

```vb
Function CreateCircle( _
   ByVal Center As MathPoint, _
   ByVal Normal As MathVector, _
   ByVal Radius As System.Double _
) As MathCircArc
```

### C#

```csharp
MathCircArc CreateCircle(
   MathPoint Center,
   MathVector Normal,
   System.double Radius
)
```

### JScript

```
function CreateCircle(
   Center : MathPoint,
   Normal : MathVector,
   Radius : System.double
) : MathCircArc;
```

### Managed Extensions for C++

```
MathCircArc* CreateCircle(
   MathPoint* Center,
   MathVector* Normal,
   System.double Radius
)
```

### C++/CLI

```cpp
MathCircArc^ CreateCircle(
   MathPoint^ Center,
   MathVector^ Normal,
   System.double Radius
)
```

### Parameters

- `Center`: Center [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `Normal`: [Vector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html) normal to the plane of the mathematical circular Arc
- `Radius`: Radius

### Return Value

[Mathematical circular Arc](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html) defining a Circle

## Examples

[Create Mathematical Circular Arcs (C#)](Create_Mathemetical_Circular_Arcs_Example_CSharp.htm)
[Create Mathematical Circular Arcs (VB.NET)](Create_Mathematical_Circular_Arcs_Example_VBNET.htm)
[Create Mathematical Circular Arcs (VBA)](Create_Mathematical_Circular_Arcs_Example_VBA.htm)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreateCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircArc.html)
[IMathUtility::CreateCircArcBy3Points Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircArcBy3Points.html)
[IMathUtility::CreateCircleBy3Points Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateCircleBy3Points.html)

## Availability

DraftSight V1R5.0
