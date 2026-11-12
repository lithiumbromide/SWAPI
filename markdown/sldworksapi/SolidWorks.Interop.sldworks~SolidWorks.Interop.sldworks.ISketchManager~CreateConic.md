---
title: "CreateConic Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateConic"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConic.html"
---

# CreateConic Method (ISketchManager)

Creates a conic curve in the active sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateConic( _
   ByVal XFocus As System.Double, _
   ByVal YFocus As System.Double, _
   ByVal ZFocus As System.Double, _
   ByVal XApex As System.Double, _
   ByVal YApex As System.Double, _
   ByVal ZApex As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim XFocus As System.Double
Dim YFocus As System.Double
Dim ZFocus As System.Double
Dim XApex As System.Double
Dim YApex As System.Double
Dim ZApex As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim value As SketchSegment

value = instance.CreateConic(XFocus, YFocus, ZFocus, XApex, YApex, ZApex, X1, Y1, Z1, X2, Y2, Z2)
```

### C#

```csharp
SketchSegment CreateConic(
   System.double XFocus,
   System.double YFocus,
   System.double ZFocus,
   System.double XApex,
   System.double YApex,
   System.double ZApex,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### C++/CLI

```cpp
SketchSegment^ CreateConic(
   System.double XFocus,
   System.double YFocus,
   System.double ZFocus,
   System.double XApex,
   System.double YApex,
   System.double ZApex,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XFocus`: X coordinate for the focus of the curve
- `YFocus`: Y coordinate for the focus of the curve
- `ZFocus`: Z coordinate for the focus of the curve
- `XApex`: X coordinate for the apex of the curve
- `YApex`: Y coordinate for the apex of the curve
- `ZApex`: Z coordinate for the apex of the curve
- `X1`: X coordinate for the start point of the curve
- `Y1`: Y coordinate for the start point of the curve
- `Z1`: Z coordinate for the start point of the curve
- `X2`: X coordinate for the end point of the curve
- `Y2`: Y coordinate for the end point of the curve
- `Z2`: Z coordinate for the end point of the curve

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the conic curve

## VBA Syntax

See [SketchManager::CreateConic](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateConic.html).

## Examples

[Insert Conic Curve Example (VBA)](Insert_Conic_Curve_Example_VB.htm)
[Insert Conic Curve (VB.NET)](Insert_Conic_Curve_Example_VBNET.htm)
[Insert Conic Curve (C#)](Insert_Conic_Curve_Example_CSharp.htm)

## Remarks

This method creates a conic curve (circle, ellipse, parabola, or hyperbola) in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using [ISketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html).

[ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) and [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

ISketchManager::AddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also significantly increases the performance of this method. When you are done creating entities, it is important to call ISketchManager::AddToDB(False), to restore SOLIDWORKS to its normal operating mode.

This method also works with ISketchManager::DisplayWhenAdded. If you have called ISketchManager::AddToDB(True), additional performance can be gained by calling ISketchManager::DisplayWhenAdded(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) or [IModelView::IGraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGraphicsRedraw.html)) to see the entities you added. You should also restore the original display settings by calling ISketchManager::DisplayWhenAdded(True).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateCircle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircle.html)
[ISketchManager::CreateEllipse Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEllipse.html)
[ISketchManager::CreateParabola Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateParabola.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
