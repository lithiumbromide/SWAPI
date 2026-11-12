---
title: "IGetLines Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "IGetLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetLines.html"
---

# IGetLines Method (ISketchBlockDefinition)

Gets information about all of the lines in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLines( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim ArraySize As System.Integer
Dim value As System.Double

value = instance.IGetLines(ArraySize)
```

### C#

```csharp
System.double IGetLines(
   System.int ArraySize
)
```

### C++/CLI

```cpp
System.double IGetLines(
   System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`: Number of lines

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISketchBlockDefinition::GetLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetLineCount.html) before calling this method to get the value for ArraySize.

The return value is the following array of doubles:

[ Color, Type, Line Font, Line Width, Layer ID, Layer Override, [Start], [End] ]

where all data values are returned as doubles:

Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

Type = line type. Valid returns as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A lineType is a combination of a lineStyle and lineWeight.

Line Font = line style. Valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).

Line Width = integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

Layer ID = integer value indicating which layer holds this entity. Obtain the [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).

Layer Override = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

Start[3] = array of 3 doubles (X,Y,Z) describing the line start point.

End[3] = array of 3 doubles (X,Y,Z) describing the line end point.

This set of data repeats for each line in the sketch. The number of doubles returned is (lineCount * 12). To determine the number of lines in the sketch, use [ISketch::GetLineCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetLineCount2.html).

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetLines.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
