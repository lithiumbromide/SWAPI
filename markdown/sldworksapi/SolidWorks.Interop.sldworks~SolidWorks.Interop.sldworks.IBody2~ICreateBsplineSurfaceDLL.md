---
title: "ICreateBsplineSurfaceDLL Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateBsplineSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurfaceDLL.html"
---

# ICreateBsplineSurfaceDLL Method (IBody2)

Creates a B-spline surface in this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBsplineSurfaceDLL( _
   ByRef Properties As System.Integer, _
   ByRef UKnotArray As System.Double, _
   ByRef VKnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Properties As System.Integer
Dim UKnotArray As System.Double
Dim VKnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Surface

value = instance.ICreateBsplineSurfaceDLL(Properties, UKnotArray, VKnotArray, ControlPointCoordArray)
```

### C#

```csharp
Surface ICreateBsplineSurfaceDLL(
   ref System.int Properties,
   ref System.double UKnotArray,
   ref System.double VKnotArray,
   ref System.double ControlPointCoordArray
)
```

### C++/CLI

```cpp
Surface^ ICreateBsplineSurfaceDLL(
   System.int% Properties,
   System.double% UKnotArray,
   System.double% VKnotArray,
   System.double% ControlPointCoordArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Properties`: Contains 8 longs (see **Remarks**)
- `UKnotArray`: Array of numUKnots doubles (see Remarks)
- `VKnotArray`: Array of numVKnots doubles (see Remarks)
- `ControlPointCoordArray`: Array of numCtrlPtCoord doubles (see Remarks)

### Return Value

New B-spline [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

## VBA Syntax

See [Body2::ICreateBsplineSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateBsplineSurfaceDLL.html).

## Remarks

You can use this method with trimming curve creation routines (for example, [ISurface::AddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~AddTrimmingLoop2.html)) to construct a trimmed surface.

The Properties argument contains the following elements. These are integers packed into a double array in the Dispatch version.

- Uorder, Vorder
- numV_CtrlPoints, numU_CtrlPoints
- Uperiodicity, Vperiodicity
- DimensionControlPoints, UNUSED ( set = 0 )

The number of elements in UKnotArray is:

```vb
numUKnots = numU_CtrlPoints + Uorder
```

The number of elements in VKnotArray is:

```vb
numVKnots = numV_CtrlPoints + Vorder
```

The number of elements in ControlPointCoordArray is :

```vb
numCtrlPtCoord =( NumV_CtrlPoints * NumU_CtrlPoints * DimensionControlPoints )
```

**NOTE:** The order of the UV control points are reversed if you used [ISurface::GetBSurfParams3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetBSurfParams3.html) or [ISurface::IGetBSurfParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IGetBSurfParams.html) to get the data. You do not need to reverse the UV control points; instead, you can switch the UV knots and related parameters.

For periodics, the first knot must have multiplicity = 1 and all excess multiplicity must be imposed on the last knot. Therefore, a valid periodic knot vector would be { 0, 1, 2, 3, 3, 3 } for a cubic curve. The control point on the seam of the closed curve cannot be replicated at both ends; it should occur only at the beginning.

To convert a clamped periodic curve (numKnots = numCtrlPts + Order, ctrlPts replicated, knot multiplicity = order at each end) to a SOLIDWORKS periodic curve, remove all but one of the knots at the beginning of the vector and remove one at the end. Also, remove the last control point to avoid the point replication.

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
