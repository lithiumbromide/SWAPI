---
title: "GetSplineEdgeData Method (IHatchBoundaryLoop)"
project: ""
interface: "IHatchBoundaryLoop"
member: "GetSplineEdgeData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetSplineEdgeData.html"
---

# GetSplineEdgeData Method (IHatchBoundaryLoop)

Gets the specified Spline data for the Hatch boundary.

## Syntax

### Visual Basic

```vb
Sub GetSplineEdgeData( _
   ByVal Index As System.Integer, _
   ByRef Degree As System.Integer, _
   ByRef Rational As System.Boolean, _
   ByRef Periodic As System.Boolean, _
   ByRef KnotValuesDblArray As System.Object, _
   ByRef ControlPointsDblArray As System.Object _
)
```

### C#

```csharp
void GetSplineEdgeData(
   System.int Index,
   out System.int Degree,
   out System.bool Rational,
   out System.bool Periodic,
   out System.object KnotValuesDblArray,
   out System.object ControlPointsDblArray
)
```

### JScript

```
function GetSplineEdgeData(
   Index : System.int,
   Degree : System.int,
   Rational : System.boolean,
   Periodic : System.boolean,
   KnotValuesDblArray : System.Object,
   ControlPointsDblArray : System.Object
);
```

### Managed Extensions for C++

```
void GetSplineEdgeData(
   System.int Index,
   [PARAMFLAG::Out] System.int Degree,
   [PARAMFLAG::Out] System.bool Rational,
   [PARAMFLAG::Out] System.bool Periodic,
   [PARAMFLAG::Out] System.Object* KnotValuesDblArray,
   [PARAMFLAG::Out] System.Object* ControlPointsDblArray
)
```

### C++/CLI

```cpp
void GetSplineEdgeData(
   System.int Index,
   [Out] System.int Degree,
   [Out] System.bool Rational,
   [Out] System.bool Periodic,
   [Out] System.Object^ KnotValuesDblArray,
   [Out] System.Object^ ControlPointsDblArray
)
```

### Parameters

- `Index`: Index of edge whose data to get (see **Remarks**)
- `Degree`: Degree of the spline
- `Rational`: True if the control points of the spline are weighted, false if not
- `Periodic`: True if periodic, false if non-periodic
- `KnotValuesDblArray`: Array of doubles of the knot values
- `ControlPointsDblArray`: Array of doubles of the control points

## Examples

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)

## Remarks

This method is valid only when [IHatchBoundaryLoop::GetEdgeType](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgeType.html) is dsHatchEdgeType_e.dsHatchEdgeType_Spline.

Before calling this method, call [IHatchBoundaryLoop::GetEdgesCount](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop~GetEdgesCount.html) to determine a valid value for Index.

## See Also

[IHatchBoundaryLoop Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop.html)
[IHatchBoundaryLoop Members](Interop.dsAutomation~Interop.dsAutomation.IHatchBoundaryLoop_members.html)

## Availability

DraftSight V1R1.3
