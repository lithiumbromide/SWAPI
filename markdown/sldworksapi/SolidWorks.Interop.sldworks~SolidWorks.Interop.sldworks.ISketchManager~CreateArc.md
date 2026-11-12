---
title: "CreateArc Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateArc.html"
---

# CreateArc Method (ISketchManager)

Creates an arc based on a center point, a start point, an end point, and a direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateArc( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
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
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim Direction As System.Short
Dim value As SketchSegment

value = instance.CreateArc(XC, YC, Zc, X1, Y1, Z1, X2, Y2, Z2, Direction)
```

### C#

```csharp
SketchSegment CreateArc(
   System.double XC,
   System.double YC,
   System.double Zc,
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
SketchSegment^ CreateArc(
   System.double XC,
   System.double YC,
   System.double Zc,
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

- `XC`: X coordinate of the circle center point in meters
- `YC`: coordinate of the circle center point in meters
- `Zc`: Z coordinate of the circle center point in meters
- `X1`: X coordinate of the start point of the arc in meters
- `Y1`: coordinate of the start point of the arc in meters
- `Z1`: Z coordinate of the start point of the arc in meters
- `X2`: X coordinate of the end point of the arc in meters
- `Y2`: Y coordinate of the end point of the arc in meters
- `Z2`: coordinate of the end point of the arc in meters
- `Direction`: +1 : Go from the start point to the end point in a counter-clockwise direction

  -1 : Go from the start point to the end point in a clockwise direction

### Return Value

[ISketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)

## VBA Syntax

See [SketchManager::CreateArc](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateArc.html).

## Examples

[Get Sketch Arc Data (VBA)](Get_Sketch_Arc_Data_Example_VB.htm)
[Get Sketch Arc Data (VB.NET)](Get_Sketch_Arc_Data_Example_VBNET.htm)
[Get Sketch Arc Data (C#)](Get_Sketch_Arc_Data_Example_CSharp.htm)

## Remarks

This method creates a partial arc in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using I[SketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html).

[ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) and [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

ISketchManager::AddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also increases the performance of this API. When you are done creating entities, it is important to call ISketchManager::AddToDB(False), to restore SOLIDWORKS to its normal operating mode.

This method also works with ISketchManager::DisplayWhenAdded. If you have called ISketchManager::AddToDB (True), additional performance can be gained by calling ISketchManager::DisplayWhenAdded(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) or [IModelView::IGraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGraphicsRedraw.html)) to see the entities that you added. You should also restore the original display settings by calling ISketchManager::DisplayWhenAdded(True).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[IModelDoc2::CreateArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArcByCenter.html)
[ISketchManager::Create3PointArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointArc.html)
[ISketchManager::CreateTangentArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateTangentArc.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
