---
title: "GetClosestPointOn Method (ICircle)"
project: ""
interface: "ICircle"
member: "GetClosestPointOn"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircle~GetClosestPointOn.html"
---

# GetClosestPointOn Method (ICircle)

Gets the point on the Circle that is closest to the specified point.

## Syntax

### Visual Basic

```vb
Sub GetClosestPointOn( _
   ByVal GivenPointX As System.Double, _
   ByVal GivenPointY As System.Double, _
   ByVal GivenPointZ As System.Double, _
   ByRef PointOnCurveX As System.Double, _
   ByRef PointOnCurveY As System.Double, _
   ByRef PointOnCurveZ As System.Double _
)
```

### C#

```csharp
void GetClosestPointOn(
   System.double GivenPointX,
   System.double GivenPointY,
   System.double GivenPointZ,
   out System.double PointOnCurveX,
   out System.double PointOnCurveY,
   out System.double PointOnCurveZ
)
```

### JScript

```
function GetClosestPointOn(
   GivenPointX : System.double,
   GivenPointY : System.double,
   GivenPointZ : System.double,
   PointOnCurveX : System.double,
   PointOnCurveY : System.double,
   PointOnCurveZ : System.double
);
```

### Managed Extensions for C++

```
void GetClosestPointOn(
   System.double GivenPointX,
   System.double GivenPointY,
   System.double GivenPointZ,
   [PARAMFLAG::Out] System.double PointOnCurveX,
   [PARAMFLAG::Out] System.double PointOnCurveY,
   [PARAMFLAG::Out] System.double PointOnCurveZ
)
```

### C++/CLI

```cpp
void GetClosestPointOn(
   System.double GivenPointX,
   System.double GivenPointY,
   System.double GivenPointZ,
   [Out] System.double PointOnCurveX,
   [Out] System.double PointOnCurveY,
   [Out] System.double PointOnCurveZ
)
```

### Parameters

- `GivenPointX`: x coordinate of the point
- `GivenPointY`: y coordinate of the point
- `GivenPointZ`: z coordinate of the point
- `PointOnCurveX`: x coordinate of the point on the Circle that is closest to the specified point
- `PointOnCurveY`: y coordinate of the point on the Circle that is closest to the specified point
- `PointOnCurveZ`: z coordinate of the point on the Circle that is closest to the specified point

## Examples

[Add Temporary Entities to Block Definition (C#)](Add_Temporary_Entities_to_Block_Definition_Example_CSharp.htm)
[Add Temporary Entities to Block Definition (VB.NET)](Add_Temporary_Entities_to_Block_Definition_Example_VBNET.htm)
[Add Temporary Entities to Block Definition (VBA)](Add_Temporary_Entities_to_Block_Definition_Example_VBA.htm)

## See Also

[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[ICircle Members](Interop.dsAutomation~Interop.dsAutomation.ICircle_members.html)
[ICircle::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~EvaluateAtDistance.html)
[ICircle::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~EvaluateAtParameter.html)
[ICircle::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~EvaluateAtPoint.html)
[ICircle::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~GetEndParams.html)
[ICircle::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~GetLength.html)

## Availability

DraftSight V1R1.3
