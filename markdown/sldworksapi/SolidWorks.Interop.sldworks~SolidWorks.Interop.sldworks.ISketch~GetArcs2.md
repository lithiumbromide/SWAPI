---
title: "GetArcs2 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetArcs2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetArcs2.html"
---

# GetArcs2 Method (ISketch)

Gets all of the arcs in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcs2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetArcs2()
```

### C#

```csharp
System.object GetArcs2()
```

### C++/CLI

```cpp
System.Object^ GetArcs2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles containing the arcs in the sketch (see **Remarks**)

## VBA Syntax

See [Sketch::GetArcs2](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetArcs2.html).

## Examples

[Get Arcs in Sketch (VBA)](Get_Arcs_in_Sketch_Example_VB.htm)

## Remarks

To determine the number of arcs, use [ISketch::GetArcCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetArcCount.html).

Return value is an array of doubles with the format:

[ Color, Type, Line Font, Line Width, Layer ID, Layer Override, [Start], [End], [Center] Rotation Dir ]

where

- Color - COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- Type - Line type. Valid returns as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A line type is a combination of a line style and line weight.
- Line Font - Line style. Valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration.
- Line Width - Integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).
- Layer ID - Integer value indicating which layer holds this entity. The [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).
- Layer Override - Integer with bit flags set to determine which properties, if any, have been overridden with respect to the layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if Layer Override was returned as 3, the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- Start[3] - An array of 3 doubles (X,Y,Z) describing the start point.
- End[3] - An array of 3 doubles (X,Y,Z) describing the end point. If the arc is closed, then End[3] is the same point as the Start.
- Center[3] - An array of 3 doubles (X,Y,Z) describing the center point.
- Rotation Dir - Rotational direction (CW = -1, CCW = 1)

This set of data repeats for each arc in the sketch. The size of the array is (NumArcs * 16).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IGetArcs2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetArcs2.html)
[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
