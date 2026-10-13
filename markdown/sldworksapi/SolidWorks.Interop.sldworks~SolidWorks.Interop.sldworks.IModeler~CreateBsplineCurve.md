---
title: "CreateBsplineCurve Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateBsplineCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve.html"
---

# CreateBsplineCurve Method (IModeler)

Creates a b-spline curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBsplineCurve( _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object

value = instance.CreateBsplineCurve(Props, Knots, CtrlPtCoords)
```

### C#

```csharp
System.object CreateBsplineCurve(
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

### C++/CLI

```cpp
System.Object^ CreateBsplineCurve(
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Props`: Array containing 4 integers packed into 2 double elements (see **Remarks**)
- `Knots`: Array of numKnots doubles (see Remarks)
- `CtrlPtCoords`: Array of NumCtrlPtCoord doubles (see Remarks)

### Return Value

B-spline [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Modeler::CreateBsplineCurve](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateBsplineCurve.html).

## Remarks

The Props argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

| Length of this array... | Given by... |
| --- | --- |
| Knots | numKnots = NumCtrlPoints + Order |
| CtrlPtCoords | NumCtrlPtCoord = NumCtrlPoints + DimensionControlPoints |

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ICreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve.html)
[IBody2::AddProfileBspline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBspline.html)
[IBody2::IAddProfileBspline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBspline.html)
