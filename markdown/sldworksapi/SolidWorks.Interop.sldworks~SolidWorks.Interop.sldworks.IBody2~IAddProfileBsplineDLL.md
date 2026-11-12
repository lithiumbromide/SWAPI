---
title: "IAddProfileBsplineDLL Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IAddProfileBsplineDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBsplineDLL.html"
---

# IAddProfileBsplineDLL Method (IBody2)

Adds a profile B-spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileBsplineDLL( _
   ByRef Properties As System.Integer, _
   ByRef KnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Properties As System.Integer
Dim KnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Curve

value = instance.IAddProfileBsplineDLL(Properties, KnotArray, ControlPointCoordArray)
```

### C#

```csharp
Curve IAddProfileBsplineDLL(
   ref System.int Properties,
   ref System.double KnotArray,
   ref System.double ControlPointCoordArray
)
```

### C++/CLI

```cpp
Curve^ IAddProfileBsplineDLL(
   System.int% Properties,
   System.double% KnotArray,
   System.double% ControlPointCoordArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Properties`: Contains 4 longs (see **Remarks**)
- `KnotArray`: Pointer to an array of numKnots doubles (see **Remarks**)
- `ControlPointCoordArray`: Pointer to an array of numCtrlPtCoord doubles (see **Remarks**)

### Return Value

Pointer to the profile B-spline [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Body2::IAddProfileBsplineDLL](ms-its:sldworksapivb6.chm::/sldworks~Body2~IAddProfileBsplineDLL.html).

## Remarks

You can use this method with [IBody2::ICreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateRevolutionSurface.html) to generate any surface
of revolution or with [IBody2::ICreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateExtrusionSurface.html) to generate a tabulated cylinder.

The Properties argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

The length of the KnotArray argument is:

numKnots = NumCtrlPoints + Order

The length of the ControlPointCoordArray is:

numCtrlPtCoord = NumCtrlPoints * DimensionControlPoints

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
