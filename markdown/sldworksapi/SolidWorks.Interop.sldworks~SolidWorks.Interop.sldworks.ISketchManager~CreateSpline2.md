---
title: "CreateSpline2 Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateSpline2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline2.html"
---

# CreateSpline2 Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::CreateSpline3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSpline2( _
   ByVal PointData As System.Object, _
   ByVal SimulateNaturalEnds As System.Boolean _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim PointData As System.Object
Dim SimulateNaturalEnds As System.Boolean
Dim value As SketchSegment

value = instance.CreateSpline2(PointData, SimulateNaturalEnds)
```

### C#

```csharp
SketchSegment CreateSpline2(
   System.object PointData,
   System.bool SimulateNaturalEnds
)
```

### C++/CLI

```cpp
SketchSegment^ CreateSpline2(
   System.Object^ PointData,
   System.bool SimulateNaturalEnds
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointData`: Array of X,Y,Z point coordinates to use in creating the spline (see **Remarks**)
- `SimulateNaturalEnds`: True to simulate natural ends, false to not simulate natural ends

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the spline

## VBA Syntax

See [SketchManager::CreateSpline2](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateSpline2.html).

## Examples

[Insert a Composite Curve (C#)](Insert_a_Composite_Curve_Example_CSharp.htm)
[Insert a Composite Curve (VB.NET)](Insert_a_Composite_Curve_Example_VBNET.htm)
[Insert a Composite Curve (VBA)](Insert_a_Composite_Curve_Example_VB.htm)

## Remarks

This method creates a spline in the active 2D sketch. If a sketch is not active, then a new sketch is created. Use [ISketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html) to check if the sketch active.

The PointData array is a set of, at least, two X, Y, Z values. For example, in VBA and VB.NET, the X value for the start point of the spline is PointData[0], the Y value for the start point is PointData[1], and the Z value for the start point is PointData[2]. The X value for the next point is PointData[3], and so on.

This method does not work with [ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) or [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html). It always adds the spline directly to the database (as if ISketchManager::AddToDB(True) was in effect), and you must redraw your document window to see the entities that you added (as if ISketchManager::DisplayWhenAdded(False) was in effect).

In 2D sketches, SOLIDWORKS ignores the Z value in PointData.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::ICreateSpline2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline2.html)
[ISketchManager::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.html)
[ISketchManager::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.html)
[ISketchManager::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams.html)
[ISketchManager::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
