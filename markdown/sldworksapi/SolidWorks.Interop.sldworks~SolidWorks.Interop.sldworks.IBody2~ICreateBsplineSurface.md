---
title: "ICreateBsplineSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateBsplineSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurface.html"
---

# ICreateBsplineSurface Method (IBody2)

Creates a new B-spline surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBsplineSurface( _
   ByVal Props As System.Object, _
   ByVal UKnots As System.Object, _
   ByVal VKnots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Props As System.Object
Dim UKnots As System.Object
Dim VKnots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As Surface

value = instance.ICreateBsplineSurface(Props, UKnots, VKnots, CtrlPtCoords)
```

### C#

```csharp
Surface ICreateBsplineSurface(
   System.object Props,
   System.object UKnots,
   System.object VKnots,
   System.object CtrlPtCoords
)
```

### C++/CLI

```cpp
Surface^ ICreateBsplineSurface(
   System.Object^ Props,
   System.Object^ UKnots,
   System.Object^ VKnots,
   System.Object^ CtrlPtCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Props`: Array containing 8 integers (see **Remarks**)
- `UKnots`: Array of numUKnots (see **Remarks**)
- `VKnots`: Array of numVKnots (see **Remarks**)
- `CtrlPtCoords`: Array of numCtrlPtCoord (see **Remarks**)

### Return Value

[ISurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) object

## VBA Syntax

See [Body2::ICreateBsplineSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateBsplineSurface.html).

## Remarks

You can use this method with trimming curve creation routines (for example, [ISurface::IAddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IAddTrimmingLoop2.html)) to construct a trimmed surface.

The Props array contains the following elements. These are integers packed into a double array in the Dispatch version.

- Uorder, Vorder
- numV_CtrlPoints, numU_CtrlPoints
- Uperiodicity, Vperiodicity
- DimensionControlPoints, UNUSED ( set =0 )

The number of elements in the UKnots array is given by:

```vb
numUKnots = numU_CtrlPoints + Uorder
```

The number of elements in the VKnots array is given by:

```vb
numVKnots = numV_CtrlPoints + Vorder
```

The number of elements in the ctrlPtCoords array is given by:

```vb
numCtrlPtCoord =( NumV_CtrlPoints * NumU_CtrlPoints * DimensionControlPoints )
```

```vb
NOTE: The order of the UV control points are reversed if you used ISurface::GetBSurfParams3 or ISurface::IGetBSurfParams to get the data. You do not need to reverse the UV control points; instead, you can switch the UV knots and related parameters.
For periodics, the first knot must have multiplicity = 1 and all excess multiplicity must be imposed on the last knot. Therefore, a valid periodic knot vector would be { 0, 1, 2, 3, 3, 3 } for a cubic curve. The control point on the seam of the closed curve cannot be replicated at both ends; it should occur only at the beginning.
```

To convert from a clamped periodic curve (numKnots = numCtrlPts + Order, ctrlPts replicated, knot multiplicity = order at each end) to a SOLIDWORKS periodic curve, remove all but one of the knots at the beginning of the vector and remove one at the end. Also remove the last control point to avoid the point replication.

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreateBsplineSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBsplineSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
