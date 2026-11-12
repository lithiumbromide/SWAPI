---
title: "GetEllipses3 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetEllipses3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetEllipses3.html"
---

# GetEllipses3 Method (ISketch)

Gets all of the ellipses in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEllipses3() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetEllipses3()
```

### C#

```csharp
System.object GetEllipses3()
```

### C++/CLI

```cpp
System.Object^ GetEllipses3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Sketch::GetEllipses3](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetEllipses3.html).

## Remarks

See [ISketch::GetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchSegments.html) or [ISketch::IEnumSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IEnumSketchSegments.html) for access to individual [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) and [ISketchEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse.html) objects.

The return values are in an array of doubles:

[ Color, LineType, LineFont, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3],Direction ... ]

where:

| Color : | COLORREF returned as an integer. Return value could be 0 or -1 for default color. |
| --- | --- |
| LineType : | Line type. Valid returns are defined in swLineTypes_e . A line type is a combination of a lineStyle and lineWeight. |
| LineFont : | Value is used for polyline font information. This value can be used as an input to the IDrawingDoc::GetLineFontInfo2 and IDrawinDoc::GetLineFontName2 . |
| LineWidth : | Integer value defining the line width. Valid width values as defined in swLineWeights_e . |
| LayerID: | Integer value indicating which layer holds this entity. Obtain the ILayer object by passing this integer value to ILayerMgr::GetLayerById or ILayerMgr::IGetLayerById . |
| LayerOverride: | Integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer. |
| StartPt[3] : | Array of 3 doubles (X,Y,Z) describing the ellipse start point |
| EndPt[3] : | Array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse is closed, then this will be the same point as the StartPt. |
| CenterPt[3] : | Array of 3 doubles (X,Y,Z) describing the ellipse center point. |
| MajorPt[3] : | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the major axis. |
| MinorPt[3] : | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the minor axis. |
| Direction : | -1 for clockwise, +1 for counterclockwise |

This set of data repeats for each ellipse in the sketch. The size of the array is (NumEllipses * 20).

To determine the number of ellipses, use [ISketch::GetEllipseCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetEllipseCount.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IGetEllipses3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetEllipses3.html)
[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
