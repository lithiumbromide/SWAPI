---
title: "GetArcs Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetArcs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetArcs.html"
---

# GetArcs Method (ISketchBlockDefinition)

Gets information about all of the arcs in the block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcs() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Object

value = instance.GetArcs()
```

### C#

```csharp
System.object GetArcs()
```

### C++/CLI

```cpp
System.Object^ GetArcs();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing an array of doubles (see **Remarks**)

## VBA Syntax

See [SketchBlockDefinition::GetArcs](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetArcs.html).

## Remarks

Return value is an array of doubles with the format:

[ Color, Type, Line Font, Line Width, Layer ID, Layer Override, [Start], [End], [Center] Rotation Dir ]

where

- Color - COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- Type - Line type. Valid returns as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A LineType is a combination of a line style and line weight.
- Line Font - Line style. Valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration.
- Line Width - Integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).
- Layer ID - Integer value indicating which layer holds this entity. The [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).
- Layer Override - Integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- Start[3] - An array of 3 doubles (X,Y,Z) describing the start point.
- End[3] - An array of 3 doubles (X,Y,Z) describing the end point. If the arc is closed, then End[3] is the same point as Start.
- Center[3] - An array of 3 doubles (X,Y,Z) describing the center point.
- Rotation Dir - Rotational direction (CW = -1, CCW = 1)

This set of data repeats for each arc in the sketch. The size of the array is (NumArcs * 16).

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::IGetArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetArcs.html)
[ISketchBlockDefinition::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetArcCount.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
