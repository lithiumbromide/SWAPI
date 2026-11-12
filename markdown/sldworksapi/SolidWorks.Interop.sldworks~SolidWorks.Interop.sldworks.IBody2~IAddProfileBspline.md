---
title: "IAddProfileBspline Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IAddProfileBspline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBspline.html"
---

# IAddProfileBspline Method (IBody2)

Creates an B-spline profile curve and returns a pointer to that curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileBspline( _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As Curve

value = instance.IAddProfileBspline(Props, Knots, CtrlPtCoords)
```

### C#

```csharp
Curve IAddProfileBspline(
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

### C++/CLI

```cpp
Curve^ IAddProfileBspline(
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Props`: Contains four integers packed into two double elements (see **Remarks**)
- `Knots`: Array of numKnots (see **Remarks**)
- `CtrlPtCoords`: Array of numCtrlPtCoord (see **Remarks**)

### Return Value

[ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Body2::IAddProfileBspline](ms-its:sldworksapivb6.chm::/sldworks~Body2~IAddProfileBspline.html).

## Remarks

You can use this method with [IBody2::ICreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateRevolutionSurface.html) to generate any surface of revolution or with [IBody2::ICreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateExtrusionSurface.html) to generate a tabulated cylinder.

The Props argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

The length of the knots array is given by:

numKnots = NumCtrlPoints + Order

The length of the CtrlPtCoords is given by:

numCtrlPtCoord = NumCtrlPoints + DimensionControlPoints

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::AddProfileBspline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBspline.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
