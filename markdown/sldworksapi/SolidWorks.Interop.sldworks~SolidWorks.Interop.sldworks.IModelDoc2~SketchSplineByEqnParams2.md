---
title: "SketchSplineByEqnParams2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchSplineByEqnParams2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSplineByEqnParams2.html"
---

# SketchSplineByEqnParams2 Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateSplineByEqnParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchSplineByEqnParams2( _
   ByVal ParamsIn As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ParamsIn As System.Object
Dim value As System.Boolean

value = instance.SketchSplineByEqnParams2(ParamsIn)
```

### C#

```csharp
System.bool SketchSplineByEqnParams2(
   System.object ParamsIn
)
```

### C++/CLI

```cpp
System.bool SketchSplineByEqnParams2(
   System.Object^ ParamsIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamsIn`: Array containing an array of doubles (see **Remarks**)

### Return Value

True if created successfully, false if not

## VBA Syntax

See [ModelDoc2::SketchSplineByEqnParams2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchSplineByEqnParams2.html).

## Examples

[Sketch a Spline (VBA)](Sketch_Spline_Example_VB.htm)

## Remarks

The parameters are provided as 3 arrays, which for OLE automation are packed into a single SafeArray packed as follows:

[ Dimension, Order, Number of control Points, Periodicity, knot1, knot2,...,ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

Pass control point coordinates to this method in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your b-curve parameters to sketch space with the help of [ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html).

NOTE: If the spline being generated is a closed spline, then it must be flagged as periodic. In addition, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created. If your data is not G1 continuous, then you must split the spline into multiple G1 segments and call method for each segment.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ISketchSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISketchSplineByEqnParams.html)
[IModelDoc2::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplineByEqnParams.html)
[IModelDoc2::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplinesByEqnParams.html)
[IModelDoc2::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplineByEqnParams.html)
[IModelDoc2::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
