---
title: "CreateSplinesByEqnParams Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateSplinesByEqnParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplinesByEqnParams.html"
---

# CreateSplinesByEqnParams Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateSplinesByEqnParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSplinesByEqnParams( _
   ByVal ParamsIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ParamsIn As System.Object
Dim value As System.Object

value = instance.CreateSplinesByEqnParams(ParamsIn)
```

### C#

```csharp
System.object CreateSplinesByEqnParams(
   System.object ParamsIn
)
```

### C++/CLI

```cpp
System.Object^ CreateSplinesByEqnParams(
   System.Object^ ParamsIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamsIn`: Array containing an array of doubles to use in creating the spline (see **Remarks**)

### Return Value

Array containing an array of objects of the newly created splines

## VBA Syntax

See [ModelDoc2::CreateSplinesByEqnParams](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateSplinesByEqnParams.html).

## Remarks

The parameters are provided as three arrays, which for OLE automation are packed into a single SafeArray, which is packed as follows:

[ Dimension, Order, Number of control Points, Periodicity, knot1, knot2,...,ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

Pass the control point coordinates to this routine in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your B-curve parameters to sketch space using [ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html).

NOTE: If the generated spline is a closed spline, then it must be flagged as periodic. Additionally, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created. If your data is not G1 continuous, then you must split the spline into multiple G1 segments and call this method for each segment.

For the OLE interface, you can use the returned object pointer directly to call any APIs on the [ISketchSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline.html) interface or its base class, [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html).

This method does not work with [IModelDoc2::SetAddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetAddToDB.html) or [IModelDoc2::SetDisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.html). It always adds the spline directly to the database (as if IModelDoc2::SetAddToDB(True) is in effect), and you must redraw your document window to see the entities that you added (as if IModelDoc2::SetDisplayWhenAdded(false) is in effect).

To create 3D splines, see [IModelDoc2::InsertCurveFilePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.html) and related functions.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSpline.html)
[IModelDoc2::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplineByEqnParams.html)
[IModelDoc2::ICreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSpline.html)
[IModelDoc2::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplineByEqnParams.html)
[IModelDoc2::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.html)
[IModelDoc2::InsertCurveFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFile.html)
[IModelDoc2::InsertCurveFileBegin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileBegin.html)
[IModelDoc2::InsertCurveFileEnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileEnd.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
