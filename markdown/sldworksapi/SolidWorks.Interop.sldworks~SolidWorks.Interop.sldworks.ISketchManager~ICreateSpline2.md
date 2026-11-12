---
title: "ICreateSpline2 Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "ICreateSpline2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline2.html"
---

# ICreateSpline2 Method (ISketchManager)

Creates a spline passing through the given points.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSpline2( _
   ByVal PointCount As System.Integer, _
   ByRef PointData As System.Double, _
   ByVal SimulateNaturalEnds As System.Boolean _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim PointCount As System.Integer
Dim PointData As System.Double
Dim SimulateNaturalEnds As System.Boolean
Dim value As SketchSegment

value = instance.ICreateSpline2(PointCount, PointData, SimulateNaturalEnds)
```

### C#

```csharp
SketchSegment ICreateSpline2(
   System.int PointCount,
   ref System.double PointData,
   System.bool SimulateNaturalEnds
)
```

### C++/CLI

```cpp
SketchSegment^ ICreateSpline2(
   System.int PointCount,
   System.double% PointData,
   System.bool SimulateNaturalEnds
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointCount`: Number of points in the spline
- `PointData`: - in-process, unmanaged C++: Pointer to an array of X,Y,Z point coordinates to use in creating the spline (see Remarks)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `SimulateNaturalEnds`: True to simulate natural ends, false to not

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the spline

## Remarks

This method creates a spline in the active 2D sketch. If a sketch is not active, then a new sketch is created. Use [ISketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html) to check if the sketch active.

The PointData array is a set of, at least, two X, Y, Z values. The X value for the start point of the spline is PointData[0], the Y value for the start point is PointData[1], and the Z value for the start point is PointData[2]. The X value for the next point is PointData[3], and so on.

This method does not work with [ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) or [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html). It always adds the spline directly to the database (as if ISketchManager::AddToDB(True) was in effect), and you must redraw your document window to see the entities that you added (as if ISketchManager::DisplayWhenAdded(False) was in effect).

In 2D sketches, SOLIDWORKS ignores the Z value in PointData.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateSpline2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline2.html)
[ISketchManager::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.html)
[ISketchManager::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.html)
[ISketchManager::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams.html)
[ISketchManager::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
