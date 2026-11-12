---
title: "ICreateEllipticalArc2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreateEllipticalArc2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArc2.html"
---

# ICreateEllipticalArc2 Method (IModelDoc2)

Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateEllipticalArc2( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal CenterZ As System.Double, _
   ByVal MajorX As System.Double, _
   ByVal MajorY As System.Double, _
   ByVal MajorZ As System.Double, _
   ByVal MinorX As System.Double, _
   ByVal MinorY As System.Double, _
   ByVal MinorZ As System.Double, _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double, _
   ByVal EndZ As System.Double _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim CenterZ As System.Double
Dim MajorX As System.Double
Dim MajorY As System.Double
Dim MajorZ As System.Double
Dim MinorX As System.Double
Dim MinorY As System.Double
Dim MinorZ As System.Double
Dim StartX As System.Double
Dim StartY As System.Double
Dim StartZ As System.Double
Dim EndX As System.Double
Dim EndY As System.Double
Dim EndZ As System.Double
Dim value As SketchSegment

value = instance.ICreateEllipticalArc2(CenterX, CenterY, CenterZ, MajorX, MajorY, MajorZ, MinorX, MinorY, MinorZ, StartX, StartY, StartZ, EndX, EndY, EndZ)
```

### C#

```csharp
SketchSegment ICreateEllipticalArc2(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double MajorX,
   System.double MajorY,
   System.double MajorZ,
   System.double MinorX,
   System.double MinorY,
   System.double MinorZ,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
)
```

### C++/CLI

```cpp
SketchSegment^ ICreateEllipticalArc2(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double MajorX,
   System.double MajorY,
   System.double MajorZ,
   System.double MinorX,
   System.double MinorY,
   System.double MinorZ,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CenterX`: X coordinate for the ellipse center point
- `CenterY`: Y coordinate for the ellipse center point
- `CenterZ`: Z coordinate for the ellipse center point
- `MajorX`: Y coordinate for a point on the ellipse and on the major axis
- `MajorY`: Y coordinate for a point on the ellipse and on the major axis
- `MajorZ`: Z coordinate for a point on the ellipse and on the major axis
- `MinorX`: X coordinate for a point on the ellipse and on the minor axis
- `MinorY`: Y coordinate for a point on the ellipse and on the minor axis
- `MinorZ`: Z coordinate for a point on the ellipse and on the minor axis
- `StartX`: X coordinate for counter clockwise elliptical arc start point
- `StartY`: Y coordinate for counter clockwise elliptical arc start point
- `StartZ`: Z coordinate for counter clockwise elliptical arc start point
- `EndX`: X coordinate for counter clockwise elliptical arc end point
- `EndY`: Y coordinate for counter clockwise elliptical arc end point
- `EndZ`: Z coordinate for counter clockwise elliptical arc end point

### Return Value

Newly created [ellipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [ModelDoc2::ICreateEllipticalArc2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreateEllipticalArc2.html).

## Remarks

This method creates a partial arc in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using [IModelDoc2::GetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetActiveSketch2.html) or [IModelDoc2::IGetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html).

For COM applications, the object pointer returned from this method can be used to call any APIs on the [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) interface. The underlying [ISketchArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc.html) object can be obtained using QueryInterface on the returned ISketchSegment object.

OLE applications can define a new ISketchSegment or ISketchArc object using the returned Dispatch pointer. Visual Basic applications interpret the pointer for you automatically, so you can use the returned object to call ISketchSegment or ISketchArc functions.

[IModelDoc2::SetAddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetAddToDB.html) and [IModelDoc2::SetDisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.html) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

- IModelDoc2::SetAddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also increases the performance of this API. When you are done creating entities, it is important to call IModelDoc2::SetAddToDB(false), to restore SOLIDWORKS to its normal operating mode.
- This method also works with IModelDoc2::SetDisplayWhenAdded. If you have called IModelDoc2::SetAddToDB(True), additional performance can be gained by calling IModelDoc2::SetDisplayWhenAdded(false) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html)) to see the entities that you added. You should also restore the original display settings by calling IModelDoc2::SetDisplayWhenAdded(True).

To create a complete ellipse, use [IModelDoc2::CreateEllipse2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateEllipse2.html) or [IModelDoc2::ICreateEllipse2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateEllipse2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreateEllipticalArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArc2.html)
[IModelDoc2::CreateEllipticalArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenter.html)
[IModelDoc2::CreateEllipticalArcByCenterVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenterVB.html)
[IModelDoc2::ICreateEllipticalArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArcByCenter.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
