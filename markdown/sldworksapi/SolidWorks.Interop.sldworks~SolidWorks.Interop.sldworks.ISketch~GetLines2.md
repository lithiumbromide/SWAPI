---
title: "GetLines2 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetLines2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetLines2.html"
---

# GetLines2 Method (ISketch)

Gets all of the lines in the sketch with an option to include or exclude crosshatch lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLines2( _
   ByVal CrossHatchOption As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim CrossHatchOption As System.Short
Dim value As System.Object

value = instance.GetLines2(CrossHatchOption)
```

### C#

```csharp
System.object GetLines2(
   System.short CrossHatchOption
)
```

### C++/CLI

```cpp
System.Object^ GetLines2(
   System.short CrossHatchOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CrossHatchOption`: Crosshatch option as defined in [swCrossHatchFilter_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCrossHatchFilter_e.html)

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Sketch::GetLines2](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetLines2.html).

## Examples

[Get Lines in Sketch (VBA)](Get_Lines_in_Sketch_Example_VB.htm)

## Remarks

The return value is the following array of doubles:

[ Color, Type, Line Font, Line Width, Layer ID, Layer Override, [Start], [End] ]

where all data values are returned as doubles:

Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

Type = line type. Valid returns as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A line type is a combination of a line style and line weight.

Line Font = line style. Valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).

Line Width = integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

Layer ID = integer value indicating which layer holds this entity. Obtain the [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).

Layer Override = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

Start[3] = array of 3 doubles (X,Y,Z) describing the line start point.

End[3] = array of 3 doubles (X,Y,Z) describing the line end point.

This set of data repeats for each line in the sketch. The number of doubles returned is (lineCount * 12). To determine the number of lines in the sketch, use [ISketch::GetLineCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetLineCount2.html).

See [ISketch::GetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchSegments.html) or [ISketch::IEnumSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IEnumSketchSegments.html) for access to individual [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) and [ISketchLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchLine.html) objects.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IGetLines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetLines2.html)
[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
