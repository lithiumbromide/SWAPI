---
title: "CreateSpline3 Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateSpline3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline3.html"
---

# CreateSpline3 Method (ISketchManager)

Creates either a 2D spline or a spline constrained to a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSpline3( _
   ByVal PointData As System.Object, _
   ByVal Surfs As System.Object, _
   ByVal Direction As System.Object, _
   ByVal SimulateNaturalEnds As System.Boolean, _
   ByRef Status As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim PointData As System.Object
Dim Surfs As System.Object
Dim Direction As System.Object
Dim SimulateNaturalEnds As System.Boolean
Dim Status As System.Object
Dim value As System.Object

value = instance.CreateSpline3(PointData, Surfs, Direction, SimulateNaturalEnds, Status)
```

### C#

```csharp
System.object CreateSpline3(
   System.object PointData,
   System.object Surfs,
   System.object Direction,
   System.bool SimulateNaturalEnds,
   out System.object Status
)
```

### C++/CLI

```cpp
System.Object^ CreateSpline3(
   System.Object^ PointData,
   System.Object^ Surfs,
   System.Object^ Direction,
   System.bool SimulateNaturalEnds,
   [Out] System.Object^ Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointData`: Array of X,Y,Z coordinates of the spline points (see **Remarks**)
- `Surfs`: Array of [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html) objects; null or Nothing for 2D splines (see **Remarks**)
- `Direction`: Array of [IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html) objects; valid only for on-surface splines (see **Remarks**)
- `SimulateNaturalEnds`: True to simulate natural ends, false to not; valid only for 2D splines (see **Remarks**)
- `Status`: Array of boolean values; empty for 2D splines (see **Remarks**)

### Return Value

[ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html) or null if an error

## VBA Syntax

See [SketchManager::CreateSpline3](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateSpline3.html).

## Examples

[Create On-surface Spline (VBA)](Create_On-surface_Spline_Example_VB.htm)
[Create On-surface Spline (VB.NET)](Create_On-surface_Spline_Example_VBNET.htm)
[Create On-surface Spline (C#)](Create_On-surface_Spline_Example_CSharp.htm)

## Remarks

This method allows you to create:

- 2D splines.
- On-surface splines as can also be created using **Tools > Sketch Entities > Spline on Surface**.

To create a 2D spline, specify:

- PointData with at least six coordinates (for the start and end points of the spline):

  [`start_pt_x, start_pt_y, start_pt_z, end_pt_x, end_pt_y, end_pt_z`]

  For 2D sketches, SOLIDWORKS assumes PointData contains no Z values.
- SimulateNaturalEnds with true for zero curvature end conditions or false to maintain curvature at the ends.
- All other parameters with null or Nothing.

To create an on-surface spline, specify:

- PointData with two or more points anywhere in 3D space. Each spline point will project onto a surface in the Surf array, depending on the direction vector specified for each point in the Direction array.
- Surf with an array of surfaces onto which the PointData is projected.
- Direction with an array of vectors, which are projection directions for every point in the PointData array. If Direction is Nothing or null, then the view vector for the current screen view is used to project each point onto a surface.

For on-surface splines only, Status contains an array of statuses, one for each point in PointArray. True indicates that the point successfully projects onto one of the surfaces. False indicates either:

- the point does not "hit" any of the specified surfaces using the direction that the point is mapped to in the Direction array,

- or -

- the spline cannot be continued at that point where the surfaces are no longer contiguous.

This method:

- Creates the 2D spline in the active sketch. If a sketch is not active, then a new sketch is created. Use [ISketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html) to check if the sketch active.
- Creates a new 3D sketch to create the on-surface spline. Call [ISketchManager::InsertSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.html) to finalize the sketch.
- Does not work with [ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) or [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html). It always adds the spline directly to the database (as if ISketchManager::AddToDB(True) was in effect), and you must redraw your document window to see the entities that you added (as if ISketchManager::DisplayWhenAdded(False) was in effect).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateSplineByEqnParams Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.html)
[ISketchManager::CreateSplinesByEqnParams2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams2.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
