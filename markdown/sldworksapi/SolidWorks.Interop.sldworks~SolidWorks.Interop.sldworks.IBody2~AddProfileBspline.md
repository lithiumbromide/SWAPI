---
title: "AddProfileBspline Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "AddProfileBspline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBspline.html"
---

# AddProfileBspline Method (IBody2)

Creates an B-spline profile curve and returns a pointer to that curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddProfileBspline( _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object

value = instance.AddProfileBspline(Props, Knots, CtrlPtCoords)
```

### C#

```csharp
System.object AddProfileBspline(
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

### C++/CLI

```cpp
System.Object^ AddProfileBspline(
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Props`: Contains 4 integers packed into 2 double elements (see **Remarks**)
- `Knots`: Array of numKnots (see Remarks)
- `CtrlPtCoords`: Array of numCtrlPtCoord (see Remarks)

### Return Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Body2::AddProfileBspline](ms-its:sldworksapivb6.chm::/sldworks~Body2~AddProfileBspline.html).

## Examples

[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)

## Remarks

You can use this method with [IBody2::CreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateRevolutionSurface.html) to generate any surface of revolution or with [IBody2::CreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateExtrusionSurface.html) to generate a tabulated cylinder.

The Props argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

The length of the knots array is given by:

numKnots = NumCtrlPoints + Order

The length of the CtrlPtCoords is given by:

NumCtrlPtCoord = NumCtrlPoints + DimensionControlPoints

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IAddProfileBspline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBspline.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
