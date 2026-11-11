---
title: "GetArcEdgeData Method (IHatchBoundaryLoop)"
project: ""
interface: "IHatchBoundaryLoop"
member: "GetArcEdgeData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetArcEdgeData.html"
---

# GetArcEdgeData Method (IHatchBoundaryLoop)

Gets the specified Arc edge data for the Hatch boundary.

## Syntax

### Visual Basic

```vb
Sub GetArcEdgeData( _
   ByVal Index As System.Integer, _
   ByRef CenterX As System.Double, _
   ByRef CenterY As System.Double, _
   ByRef Radius As System.Double, _
   ByRef StartAngle As System.Double, _
   ByRef EndAngle As System.Double, _
   ByRef IsCounterclockwiseFlag As System.Boolean _
)
```

### C#

```csharp
void GetArcEdgeData(
   System.int Index,
   out System.double CenterX,
   out System.double CenterY,
   out System.double Radius,
   out System.double StartAngle,
   out System.double EndAngle,
   out System.bool IsCounterclockwiseFlag
)
```

### JScript

```
function GetArcEdgeData(
   Index : System.int,
   CenterX : System.double,
   CenterY : System.double,
   Radius : System.double,
   StartAngle : System.double,
   EndAngle : System.double,
   IsCounterclockwiseFlag : System.boolean
);
```

### Managed Extensions for C++

```
void GetArcEdgeData(
   System.int Index,
   [PARAMFLAG::Out] System.double CenterX,
   [PARAMFLAG::Out] System.double CenterY,
   [PARAMFLAG::Out] System.double Radius,
   [PARAMFLAG::Out] System.double StartAngle,
   [PARAMFLAG::Out] System.double EndAngle,
   [PARAMFLAG::Out] System.bool IsCounterclockwiseFlag
)
```

### C++/CLI

```cpp
void GetArcEdgeData(
   System.int Index,
   [Out] System.double CenterX,
   [Out] System.double CenterY,
   [Out] System.double Radius,
   [Out] System.double StartAngle,
   [Out] System.double EndAngle,
   [Out] System.bool IsCounterclockwiseFlag
)
```

### Parameters

- `Index`: Index of the Arc edge whose data to get (see **Remarks**)
- `CenterX`: x coordinate of the Arc center
- `CenterY`: y coordinate of the Arc center
- `Radius`: Radius of the Arc from the center coordinates
- `StartAngle`: Angle from the chord that is tangent to the start point of the Arc
- `EndAngle`: Angle from the chord that is tangent to the end point of the Arc
- `IsCounterclockwiseFlag`: True if the Arc is drawn in a counterclockwise direction, false if in a clockwise direction

## Examples

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)

## Remarks

This method is valid only when [IHatchBoundaryLoop::GetEdgeType](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgeType.html) is dsHatchEdgeType_e.dsHatchEdgeType_CirArc.

Before calling this method, call [IHatchBoundaryLoop::GetEdgesCount](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgesCount.html) to determine a valid value for Index.

## See Also

[IHatchBoundaryLoop Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop.html)
[IHatchBoundaryLoop Members](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop_members.html)

## Availability

DraftSight V1R1.3
