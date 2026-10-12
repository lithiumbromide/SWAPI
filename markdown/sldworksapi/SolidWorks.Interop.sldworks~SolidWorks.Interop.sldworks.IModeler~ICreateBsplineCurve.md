---
title: "ICreateBsplineCurve Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBsplineCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve.html"
---

# ICreateBsplineCurve Method (IModeler)

Creates a b-spline curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBsplineCurve( _
   ByRef Properties As System.Integer, _
   ByRef KnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Properties As System.Integer
Dim KnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Curve

value = instance.ICreateBsplineCurve(Properties, KnotArray, ControlPointCoordArray)
```

### C#

```csharp
Curve ICreateBsplineCurve(
   ref System.int Properties,
   ref System.double KnotArray,
   ref System.double ControlPointCoordArray
)
```

### C++/CLI

```cpp
Curve^ ICreateBsplineCurve(
   System.int% Properties,
   System.double% KnotArray,
   System.double% ControlPointCoordArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Properties`: Array containing 4 integers packed into 2 double elements (see **Remarks**)
- `KnotArray`: Array of numKnots doubles (see Remarks)
- `ControlPointCoordArray`: Array of NumCtrlPtCoord doubles (see Remarks)

### Return Value

B-spline [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Modeler::ICreateBsplineCurve](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBsplineCurve.html).

## Remarks

The Properties argument contains the following values:

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
[IModeler::CreateBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve.html)
[IModeler::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.html)
[IModeler::ICreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineSurface.html)
