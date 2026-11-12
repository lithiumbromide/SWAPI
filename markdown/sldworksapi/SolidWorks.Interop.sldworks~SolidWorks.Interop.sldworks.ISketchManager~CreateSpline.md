---
title: "CreateSpline Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateSpline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline.html"
---

# CreateSpline Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::CreateSpline2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateSpline2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSpline( _
   ByVal PointData As System.Object _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim PointData As System.Object
Dim value As SketchSegment

value = instance.CreateSpline(PointData)
```

### C#

```csharp
SketchSegment CreateSpline(
   System.object PointData
)
```

### C++/CLI

```cpp
SketchSegment^ CreateSpline(
   System.Object^ PointData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointData`: Array of X,Y,Z point coordinates to use in creating the spline (see **Remarks**)

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the spline

## VBA Syntax

See [SketchManager::CreateSpline](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateSpline.html).

## Remarks

This method creates a spline in the active 2D sketch. If a sketch is not active, then a new sketch is created. Use [ISketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html) to check if the sketch active.

The PointData array is a set of, at least, two X, Y, Z values. For example, in VBA and VB.NET, the X value for the start point of the spline is PointData[0], the Y value for the start point is PointData[1], and the Z value for the start point is PointData[2]. The X value for the next point is PointData[3], and so on.

This method does not work with [ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) or [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html). It always adds the spline directly to the database (as if ISketchManager::AddToDB(True) was in effect), and you must redraw your document window to see the entities that you added (as if ISketchManager::DisplayWhenAdded(False) was in effect).

In 2D sketches, SOLIDWORKS ignores the Z value in PointData.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.html)
[ISketchManager::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.html)
[ISketchManager::ICreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline.html)
[ISketchManager::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams.html)
[ISketchManager::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
