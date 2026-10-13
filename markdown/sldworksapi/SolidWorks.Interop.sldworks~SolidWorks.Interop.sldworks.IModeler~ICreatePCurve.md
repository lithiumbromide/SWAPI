---
title: "ICreatePCurve Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreatePCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePCurve.html"
---

# ICreatePCurve Method (IModeler)

Creates a pcurve.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePCurve( _
   ByVal Surface As Surface, _
   ByRef Props As System.Integer, _
   ByRef Knots As System.Double, _
   ByRef CtrlPtCoords As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Surface As Surface
Dim Props As System.Integer
Dim Knots As System.Double
Dim CtrlPtCoords As System.Double
Dim value As Curve

value = instance.ICreatePCurve(Surface, Props, Knots, CtrlPtCoords)
```

### C#

```csharp
Curve ICreatePCurve(
   Surface Surface,
   ref System.int Props,
   ref System.double Knots,
   ref System.double CtrlPtCoords
)
```

### C++/CLI

```cpp
Curve^ ICreatePCurve(
   Surface^ Surface,
   System.int% Props,
   System.double% Knots,
   System.double% CtrlPtCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Surface`: [Surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) associated with the pcurve
- `Props`: Array containing 4 integers packed into 2 double elements (see **Remarks**)
- `Knots`: Array of numKnots (see **Remarks**)
- `CtrlPtCoords`: Array of numCtrlPtCoord (see **Remarks**)

## VBA Syntax

See [Modeler::ICreatePCurve](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreatePCurve.html).

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
[IModeler::CreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePCurve.html)
[ICurve::GetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams.html)
[ICurve::IGetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.html)
[ICurve::IGetPCurveParamsSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParamsSize.html)
[IModeler::CreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve.html)
[IModeler::ICreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
