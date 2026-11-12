---
title: "CreateEllipticalArc Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateEllipticalArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEllipticalArc.html"
---

# CreateEllipticalArc Method (ISketchManager)

Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateEllipticalArc( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal XMajor As System.Double, _
   ByVal YMajor As System.Double, _
   ByVal ZMajor As System.Double, _
   ByVal XMinor As System.Double, _
   ByVal YMinor As System.Double, _
   ByVal ZMinor As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal Direction As System.Short _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim XMajor As System.Double
Dim YMajor As System.Double
Dim ZMajor As System.Double
Dim XMinor As System.Double
Dim YMinor As System.Double
Dim ZMinor As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim Direction As System.Short
Dim value As SketchSegment

value = instance.CreateEllipticalArc(XC, YC, Zc, XMajor, YMajor, ZMajor, XMinor, YMinor, ZMinor, X1, Y1, Z1, X2, Y2, Z2, Direction)
```

### C#

```csharp
SketchSegment CreateEllipticalArc(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double XMajor,
   System.double YMajor,
   System.double ZMajor,
   System.double XMinor,
   System.double YMinor,
   System.double ZMinor,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.short Direction
)
```

### C++/CLI

```cpp
SketchSegment^ CreateEllipticalArc(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double XMajor,
   System.double YMajor,
   System.double ZMajor,
   System.double XMinor,
   System.double YMinor,
   System.double ZMinor,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.short Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XC`: X coordinate for the ellipse center point
- `YC`: Y coordinate for the ellipse center point
- `Zc`: Z coordinate for the ellipse center point
- `XMajor`: X coordinate for a point on the ellipse and on the major axis
- `YMajor`: Y coordinate for a point on the ellipse and on the major axis
- `ZMajor`: Z coordinate for a point on the ellipse and on the major axis
- `XMinor`: X coordinate for a point on the ellipse and on the minor axis
- `YMinor`: Y coordinate for a point on the ellipse and on the minor axis
- `ZMinor`: Z coordinate for a point on the ellipse and on the minor axis
- `X1`: X coordinate for counter-clockwise elliptical arc start point
- `Y1`: Y coordinate for counter-clockwise elliptical arc start point
- `Z1`: Z coordinate for counter-clockwise elliptical arc start point
- `X2`: X coordinate for counter-clockwise elliptical arc end point
- `Y2`: Y coordinate for counter-clockwise elliptical arc end point
- `Z2`: Z coordinate for counter-clockwise elliptical arc end point
- `Direction`: - +1 : Go from the start point to the end point in a counter-clockwise direction
  - -1 : Go from the start point to the end point in a clockwise direction

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the elliptical arc

## VBA Syntax

See [SketchManager::CreateEllipticalArc](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateEllipticalArc.html).

## Remarks

This method creates a full circle in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using [ISketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html).

[ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) and [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

ISketchManager::AddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also significantly increases the performance of this method. When you are done creating entities, it is important to ISketchManager::AddToDB(False), to restore SOLIDWORKS to its normal operating mode.

This method also works with ISketchManager::DisplayWhenAdded. If you have called ISketchManager::AddToDB(True), additional performance can be gained by calling ISketchManager::DisplayWhenAdded(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) or [IModelView::IGraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGraphicsRedraw.html)) to see the entities you added. You should also restore the original display settings by calling ISketchManager::DisplayWhenAdded(True).

To create a complete ellipse, use [ISketchManager::CreateEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateEllipse.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
