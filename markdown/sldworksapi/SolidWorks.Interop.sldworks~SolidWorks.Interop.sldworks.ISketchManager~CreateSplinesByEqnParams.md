---
title: "CreateSplinesByEqnParams Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateSplinesByEqnParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.html"
---

# CreateSplinesByEqnParams Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::CreateSplinesByEqnParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSplinesByEqnParams( _
   ByVal Parameters As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Parameters As System.Object
Dim value As System.Object

value = instance.CreateSplinesByEqnParams(Parameters)
```

### C#

```csharp
System.object CreateSplinesByEqnParams(
   System.object Parameters
)
```

### C++/CLI

```cpp
System.Object^ CreateSplinesByEqnParams(
   System.Object^ Parameters
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Parameters`: Array containing an array of doubles to use in creating the spline (see **Remarks**)

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) of the newly created splines

## VBA Syntax

See [SketchManager::CreateSplinesByEqnParams](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateSplinesByEqnParams.html).

## Remarks

The Properties array contains four longs (placed in the first four doubles in the array):

- Dimension
- Order
- Number of Control Points
- Periodicity ( true or false)

The Knots array contains doubles with (Number of Control Points + Order) elements.

The size of the ControlPoints array is based upon the curve dimension.

- Dimension = 2 then each Control Point is an array of 2 doubles ( x, y )
- Dimension = 3 then each Control Point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each Control Point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as three arrays.

Pass the control point coordinates to this routine in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your B-curve parameters to sketch space using [ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html).

**NOTE:** If the spline being generated is a closed spline, then it must be flagged as periodic. If the data passed to this method does not generate a G1 continuous spline, then it creates multiple G1 continuous spline segments.

This method does not work with [ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) or [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html). It always adds the spline directly to the database (as if ISketchManager::AddToDB(True) is in effect), and you must redraw your document window to see the entities that you added (as if ISketchManager::DisplayWhenAdded(False) is in effect).

To create 3D splines, see [IModelDoc2::InsertCurveFilePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.html) and related functions.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline.html)
[ISketchManager::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.html)
[ISketchManager::ICreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline.html)
[ISketchManager::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams.html)
[ISketchManager::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
