---
title: "CreatePCurve Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreatePCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePCurve.html"
---

# CreatePCurve Method (IModeler)

Creates a pcurve.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePCurve( _
   ByVal Surface As System.Object, _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Surface As System.Object
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object

value = instance.CreatePCurve(Surface, Props, Knots, CtrlPtCoords)
```

### C#

```csharp
System.object CreatePCurve(
   System.object Surface,
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

### C++/CLI

```cpp
System.Object^ CreatePCurve(
   System.Object^ Surface,
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Surface`: [Surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) associated with the pcurve
- `Props`: Array containing 4 integers packed into 2 double elements (see **Remarks**)
- `Knots`: Array of numKnots (see **Remarks**)
- `CtrlPtCoords`: Array of numCtrlPtCoord (see **Remarks**)

### Return Value

[Pcurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Modeler::CreatePCurve](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreatePCurve.html).

## Examples

[Create Space Parameter Curve On Surface (VBA)](Create_Space_Parameter_Curve_on_Surface_Example_VB.htm)

## Remarks

The Props argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

| Length of this array... | Given by... |
| --- | --- |
| Knots | numKnots = NumCtrlPoints + Order |
| CtrlPtCoords | NumCtrlPtCoord = NumCtrlPoints * DimensionControlPoints |

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ICreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePCurve.html)
[ICurve::GetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams.html)
[ICurve::IGetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.html)
[ICurve::IGetPCurveParamsSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParamsSize.html)
[IModeler::CreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve.html)
[IModeler::ICreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
