---
title: "ICreateSplineByEqnParams Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "ICreateSplineByEqnParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams.html"
---

# ICreateSplineByEqnParams Method (ISketchManager)

Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSplineByEqnParams( _
   ByRef Properties As System.Integer, _
   ByVal KnotArrayCount As System.Integer, _
   ByRef Knots As System.Double, _
   ByVal ControlPointArrayCount As System.Integer, _
   ByRef ControlPoints As System.Double _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Properties As System.Integer
Dim KnotArrayCount As System.Integer
Dim Knots As System.Double
Dim ControlPointArrayCount As System.Integer
Dim ControlPoints As System.Double
Dim value As SketchSegment

value = instance.ICreateSplineByEqnParams(Properties, KnotArrayCount, Knots, ControlPointArrayCount, ControlPoints)
```

### C#

```csharp
SketchSegment ICreateSplineByEqnParams(
   ref System.int Properties,
   System.int KnotArrayCount,
   ref System.double Knots,
   System.int ControlPointArrayCount,
   ref System.double ControlPoints
)
```

### C++/CLI

```cpp
SketchSegment^ ICreateSplineByEqnParams(
   System.int% Properties,
   System.int KnotArrayCount,
   System.double% Knots,
   System.int ControlPointArrayCount,
   System.double% ControlPoints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Properties`: - in-process, unmanaged C++: Pointer to an array of properties including dimension, order, number of control points, periodicity (see Remarks)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `KnotArrayCount`: Number of knots
- `Knots`: - in-process, unmanaged C++: Pointer to an array of knots (e.g., knot1, knot2, and so on)
  - VBA, VB.NET, C#, and C++/CLI: Not supported
- `ControlPointArrayCount`: Number of control points
- `ControlPoints`: - in-process, unmanaged C++: Pointer to an array of control points (e.g., controlpoint1[dimension], controlpoint2[dimension], and so on)

  VBA, VB.NET, C#, and C++/CLI: Not supported

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the spline

## Remarks

The Properties array contains four longs (placed in the first four doubles in the array):

- Dimension
- Order
- Number of Control Points
- Periodicity ( true or false)

The Knots array contains doubles with (Number of Control Points + Order) elements.

The size of the ControlPoints array is based upon the curve dimension.

- Dimension = 2 then each Control Point is an array of 2 doubles ( x, y )
- Dimension = 3 then each Control Point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each Control Point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as three arrays.

Pass the control point coordinates to this routine in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your B-curve parameters to sketch space using [ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html).

NOTE: The curve can be either periodic or non-periodic. If the generated spline is a closed spline, then it must be flagged as periodic. Additionally, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created. If your data is not G1 continuous, then you must split the spline into multiple G1 segments and call this method for each segment.

This method does not work with [ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) or [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html). It always adds the spline directly to the database (as if ISketchManager::AddToDB(True) is in effect), and you must redraw your document window to see the entities that you added (as if ISketchManager::DisplayWhenAdded(False) is in effect).

To create 3D splines, see [IModelDoc2::InsertCurveFilePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.html) and related functions.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline.html)
[ISketchManager::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.html)
[ISketchManager::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.html)
[ISketchManager::ICreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline.html)
[ISketchManager::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
