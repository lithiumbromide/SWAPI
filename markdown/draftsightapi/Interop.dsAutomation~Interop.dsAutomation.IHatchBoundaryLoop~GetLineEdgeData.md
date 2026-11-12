---
title: "GetLineEdgeData Method (IHatchBoundaryLoop)"
project: ""
interface: "IHatchBoundaryLoop"
member: "GetLineEdgeData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetLineEdgeData.html"
---

# GetLineEdgeData Method (IHatchBoundaryLoop)

Gets the specified Line edge data for the Hatch boundary.

## Syntax

### Visual Basic

```vb
Sub GetLineEdgeData( _
   ByVal Index As System.Integer, _
   ByRef StartPointX As System.Double, _
   ByRef StartPointY As System.Double, _
   ByRef EndPointX As System.Double, _
   ByRef EndPointY As System.Double _
)
```

### C#

```csharp
void GetLineEdgeData(
   System.int Index,
   out System.double StartPointX,
   out System.double StartPointY,
   out System.double EndPointX,
   out System.double EndPointY
)
```

### JScript

```
function GetLineEdgeData(
   Index : System.int,
   StartPointX : System.double,
   StartPointY : System.double,
   EndPointX : System.double,
   EndPointY : System.double
);
```

### Managed Extensions for C++

```
void GetLineEdgeData(
   System.int Index,
   [PARAMFLAG::Out] System.double StartPointX,
   [PARAMFLAG::Out] System.double StartPointY,
   [PARAMFLAG::Out] System.double EndPointX,
   [PARAMFLAG::Out] System.double EndPointY
)
```

### C++/CLI

```cpp
void GetLineEdgeData(
   System.int Index,
   [Out] System.double StartPointX,
   [Out] System.double StartPointY,
   [Out] System.double EndPointX,
   [Out] System.double EndPointY
)
```

### Parameters

- `Index`: Index of the Line edge whose data to get (see **Remarks**)
- `StartPointX`: x coordinate of the start point of the Line
- `StartPointY`: y coordinate of the start point of the Line
- `EndPointX`: x coordinate of the end point of the Line
- `EndPointY`: y coordinate of the end point of the Line

## Examples

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)

## Remarks

This method is valid only when [IHatchBoundaryLoop::GetEdgeType](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgeType.html) is dsHatchEdgeType_e.dsHatchEdgeType_Line.

Before calling this method, call [IHatchBoundaryLoop::GetEdgesCount](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgesCount.html) to determine a valid value for Index.

## See Also

[IHatchBoundaryLoop Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop.html)
[IHatchBoundaryLoop Members](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop_members.html)

## Availability

DraftSight V1R1.3
