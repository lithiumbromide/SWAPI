---
title: "IGetControlPoints Method (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "IGetControlPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetControlPoints.html"
---

# IGetControlPoints Method (ISplineParamData)

Gets the coordinates of all of the control points of the spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetControlPoints( _
   ByVal Count As System.Integer, _
   ByRef ControlPoints As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim Count As System.Integer
Dim ControlPoints As System.Double
Dim value As System.Boolean

value = instance.IGetControlPoints(Count, ControlPoints)
```

### C#

```csharp
System.bool IGetControlPoints(
   System.int Count,
   out System.double ControlPoints
)
```

### C++/CLI

```cpp
System.bool IGetControlPoints(
   System.int Count,
   [Out] System.double ControlPoints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Size of ControlPoints array
- `ControlPoints`: - in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if successful, false if not

## Remarks

Before calling this method, call [ISplineParamData::ControlPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~ControlPointsCount.html) to populate the Count parameter.

Control points determine the shape of a spline or curve. Starting with a set of control points, all other points of a spline can be calculated. A given point on the spline is calculated using the polynomial basis functions of its nearest control points. The [knot vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~GetKnotPoints.html) determines which control point basis functions are in force for calculating each point along a curve.

The size of the ControlPoints array is based on the curve dimension:

- if [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html) = 2 then each control point has 2 doubles ( x, y )
- if [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html) = 3 then each control point has 3 doubles ( x, y, z )
- if [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html) = 4, and the curve is closed or periodic, then each control point has 4 doubles ( x, y, z, w ), where w = weight
- if [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html) = 4, and the curve is open or non-periodic, then each control point has 4 doubles ( w*x, w*y, w*z, w ), where w = weight
- Size of ControlPoints array = [control points count](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~ControlPointsCount.html) * [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html)

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::GetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetControlPoints.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
