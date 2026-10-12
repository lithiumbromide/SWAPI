---
title: "CreateCircle Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateCircle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircle.html"
---

# CreateCircle Method (ISketchManager)

Creates a circle based on a center point and a point on the circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCircle( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Xp As System.Double, _
   ByVal Yp As System.Double, _
   ByVal Zp As System.Double _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Xp As System.Double
Dim Yp As System.Double
Dim Zp As System.Double
Dim value As SketchSegment

value = instance.CreateCircle(XC, YC, Zc, Xp, Yp, Zp)
```

### C#

```csharp
SketchSegment CreateCircle(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp
)
```

### C++/CLI

```cpp
SketchSegment^ CreateCircle(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XC`: X coordinate of the circle center point, in meters
- `YC`: Y coordinate of the circle center point, in meters
- `Zc`: Z coordinate of the circle center point, in meters
- `Xp`: X coordinate of the point on the circle, in meters
- `Yp`: Y coordinate of the point on the circle, in meters
- `Zp`: Z coordinate of the point on the circle, in meters

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the circle

## VBA Syntax

See [SketchManager::CreateCircle](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateCircle.html).

## Examples

[Create and Edit Circular Sketch Pattern (VB.NET)](Create_and_Edit_Circular_Sketch_Pattern_Example_VBNET.htm)
[Create and Edit Circular Sketch Pattern (VBA)](Create_and_Edit_Circular_Sketch_Pattern_Example_VB.htm)
[Create and Edit Circular Sketch Pattern (C#)](Create_and_Edit_Circular_Sketch_Pattern_Example_CSharp.htm)
[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## Remarks

This method creates a full circle in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using [ISketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html).

[ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) and [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

ISketchManager::AddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also significantly increases the performance of this method. When you are done creating entities, it is important to ISketchManager::AddToDB(False), to restore SOLIDWORKS to its normal operating mode.

This method also works with ISketchManager::DisplayWhenAdded. If you have called ISketchManager::AddToDB(True), additional performance can be gained by calling ISketchManager::DisplayWhenAdded(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) or [IModelView::IGraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGraphicsRedraw.html)) to see the entities you added. You should also restore the original display settings by calling ISketchManager::DisplayWhenAdded(True).

To create a circle using a center point and radius, see [ISketchManager::CreateCircleByRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateCircleByRadius.html). To create a partial arc, see [ISketchManager::CreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateArc.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateConic Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConic.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
