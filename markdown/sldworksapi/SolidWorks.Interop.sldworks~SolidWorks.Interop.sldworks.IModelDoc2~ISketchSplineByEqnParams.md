---
title: "ISketchSplineByEqnParams Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ISketchSplineByEqnParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISketchSplineByEqnParams.html"
---

# ISketchSplineByEqnParams Method (IModelDoc2)

Creates a spline on the active 2D sketch using the specified b-curve parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISketchSplineByEqnParams( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim value As System.Integer

value = instance.ISketchSplineByEqnParams(PropArray, KnotsArray, CntrlPntCoordArray)
```

### C#

```csharp
System.int ISketchSplineByEqnParams(
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray
)
```

### C++/CLI

```cpp
System.int ISketchSplineByEqnParams(
   System.int% PropArray,
   System.double% KnotsArray,
   System.double% CntrlPntCoordArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropArray`: Includes dimension, order, number of control points, and periodicity
- `KnotsArray`: knot1, knot2, and so on
- `CntrlPntCoordArray`: controlpoint1[dimension], controlpoint2[dimension], and so on

### Return Value

True if created successfully, false if not

## VBA Syntax

See [ModelDoc2::ISketchSplineByEqnParams](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ISketchSplineByEqnParams.html).

## Examples

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)

## Remarks

The PropArray argument contains 4 integers packed into the first two doubles in the array:

- Dimension
- Order
- Number of Control Points
- Periodicity ( True or false )

The KnotsArray argument is an array of doubles with (Number of Control Points + Order) elements.

The size of the CntrlPntCoordArray array is based upon the curve dimension:

- Dimension = 2 then each control point is an array of 2 doubles ( x, y )
- Dimension = 3 then each control point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each control point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as 3 arrays, which for COM applications are passed separately.

Pass control point coordinates to this method in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your b-curve parameters to sketch space with the help of [ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html).

NOTE: If the spline being generated is a closed spline, then it must be flagged as periodic. In addition, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SketchSplineByEqnParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSplineByEqnParams2.html)
[IModelDoc2::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplineByEqnParams.html)
[IModelDoc2::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplinesByEqnParams.html)
[IModelDoc2::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplineByEqnParams.html)
[IModelDoc2::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
