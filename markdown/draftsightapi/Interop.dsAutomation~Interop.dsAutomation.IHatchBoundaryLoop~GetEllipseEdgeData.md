---
title: "GetEllipseEdgeData Method (IHatchBoundaryLoop)"
project: ""
interface: "IHatchBoundaryLoop"
member: "GetEllipseEdgeData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEllipseEdgeData.html"
---

# GetEllipseEdgeData Method (IHatchBoundaryLoop)

Gets the specified Ellipse edge data for the Hatch boundary.

## Syntax

### Visual Basic

```vb
Sub GetEllipseEdgeData( _
   ByVal Index As System.Integer, _
   ByRef CenterX As System.Double, _
   ByRef CenterY As System.Double, _
   ByRef MajorAxisX As System.Double, _
   ByRef MajorAxisY As System.Double, _
   ByRef MinorAxisLengthRatio As System.Double, _
   ByRef StartAngle As System.Double, _
   ByRef EndAngle As System.Double, _
   ByRef IsCounterclockwiseFlag As System.Boolean _
)
```

### C#

```csharp
void GetEllipseEdgeData(
   System.int Index,
   out System.double CenterX,
   out System.double CenterY,
   out System.double MajorAxisX,
   out System.double MajorAxisY,
   out System.double MinorAxisLengthRatio,
   out System.double StartAngle,
   out System.double EndAngle,
   out System.bool IsCounterclockwiseFlag
)
```

### JScript

```
function GetEllipseEdgeData(
   Index : System.int,
   CenterX : System.double,
   CenterY : System.double,
   MajorAxisX : System.double,
   MajorAxisY : System.double,
   MinorAxisLengthRatio : System.double,
   StartAngle : System.double,
   EndAngle : System.double,
   IsCounterclockwiseFlag : System.boolean
);
```

### Managed Extensions for C++

```
void GetEllipseEdgeData(
   System.int Index,
   [PARAMFLAG::Out] System.double CenterX,
   [PARAMFLAG::Out] System.double CenterY,
   [PARAMFLAG::Out] System.double MajorAxisX,
   [PARAMFLAG::Out] System.double MajorAxisY,
   [PARAMFLAG::Out] System.double MinorAxisLengthRatio,
   [PARAMFLAG::Out] System.double StartAngle,
   [PARAMFLAG::Out] System.double EndAngle,
   [PARAMFLAG::Out] System.bool IsCounterclockwiseFlag
)
```

### C++/CLI

```cpp
void GetEllipseEdgeData(
   System.int Index,
   [Out] System.double CenterX,
   [Out] System.double CenterY,
   [Out] System.double MajorAxisX,
   [Out] System.double MajorAxisY,
   [Out] System.double MinorAxisLengthRatio,
   [Out] System.double StartAngle,
   [Out] System.double EndAngle,
   [Out] System.bool IsCounterclockwiseFlag
)
```

### Parameters

- `Index`: Index of the Ellipse edge whose data to get
- `CenterX`: x coordinate of the Ellipse center
- `CenterY`: y coordinate of the Ellipse center
- `MajorAxisX`: x coordinate of a point on the major axis of the Ellipse
- `MajorAxisY`: y coordinate of a point on the major axis of the Ellipse
- `MinorAxisLengthRatio`: Ratio of the length of the minor axis to the major axis
- `StartAngle`: Angle from the chord that is tangent to the start point of the Ellipse
- `EndAngle`: Angle from the chord that is tangent to the end point of the Ellipse
- `IsCounterclockwiseFlag`: True if the Ellipse is drawn in a counterclockwise direction, false if in a clockwise direction

## Examples

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)

## Remarks

This method is valid only when [IHatchBoundaryLoop::GetEdgeType](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgeType.html) is dsHatchEdgeType_e.dsHatchEdgeType_EllArc.

Before calling this method, call [IHatchBoundaryLoop::GetEdgesCount](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgesCount.html) to determine a valid value for Index.

## See Also

[IHatchBoundaryLoop Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop.html)
[IHatchBoundaryLoop Members](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop_members.html)

## Availability

DraftSight V1R1.3
