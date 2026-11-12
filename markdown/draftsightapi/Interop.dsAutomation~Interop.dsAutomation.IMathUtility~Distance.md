---
title: "Distance Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "Distance"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~Distance.html"
---

# Distance Method (IMathUtility)

Gets the distance between the specified mathematical objects. Also gets the points used to measure the distance.

## Syntax

### Visual Basic

```vb
Function Distance( _
   ByVal Object1 As System.Object, _
   ByVal Object2 As System.Object, _
   ByRef Point1 As MathPoint, _
   ByRef Point2 As MathPoint _
) As System.Double
```

### C#

```csharp
System.double Distance(
   System.object Object1,
   System.object Object2,
   out MathPoint Point1,
   out MathPoint Point2
)
```

### JScript

```
function Distance(
   Object1 : System.Object,
   Object2 : System.Object,
   Point1 : MathPoint,
   Point2 : MathPoint
) : System.double;
```

### Managed Extensions for C++

```
System.double Distance(
   System.Object* Object1,
   System.Object* Object2,
   [PARAMFLAG::Out] MathPoint* Point1,
   [PARAMFLAG::Out] MathPoint* Point2
)
```

### C++/CLI

```cpp
System.double Distance(
   System.Object^ Object1,
   System.Object^ Object2,
   [Out] MathPoint^ Point1,
   [Out] MathPoint^ Point2
)
```

### Parameters

- `Object1`: Math object (see **Remarks**)
- `Object2`: Math object (see **Remarks**)
- `Point1`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on Object1 used to measure the distance
- `Point2`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on Object2 used to measure the distance

### Return Value

Distance between the specified objects

## Examples

[Get Distance Between Two Math Points (C#)](Get_Distance_Between_Two_Math_Points_Example_CSharp.htm)
[Get Distance Between Two Math Points (VB.NET)](Get_Distance_Between_Two_Math_Points_Example_VBNET.htm)
[Get Distance Between Two Math Points (JavaScript)](Get_Distance_Between_Two_Math_Points_Example_JS.htm)
[Get Distance Between Two Math Points (VBA)](Get_Distance_Between_Two_Math_Points_Example_VBA.htm)

## Remarks

The possible Object1-Object2 distance types:

- [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) - IMathPoint
- [IMathLine](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html) - IMathPoint
- IMathLine - IMathLine
- IMathLine - [IMathCircArc](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
- IMathLine - [IMathEllipArc](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)
- IMathCircArc - IMathPoint
- IMathCircArc - IMathLine
- IMathCircArc - IMathCircArc
- IMathCircArc - IMathEllipArc
- IMathEllipArc - IMathPoint
- IMathEllipArc - IMathLine
- IMathEllipArc - IMathCircArc
- IMathEllipArc - IMathEllipArc
- [IMathPlane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html) - IMathPoint

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)

## Availability

DraftSight V1R1.4
