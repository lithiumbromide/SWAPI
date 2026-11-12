---
title: "Width Property (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "Width"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Width.html"
---

# Width Property (ISketchSegment)

Gets or sets the line width for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Integer

instance.Width = value

value = instance.Width
```

### C#

```csharp
System.int Width {get; set;}
```

### C++/CLI

```cpp
property System.int Width {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Line width used for this sketch segment as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

## VBA Syntax

See [SketchSegment::Width](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~Width.html).

## Examples

[Get Sketch Entities with Visual Properties (VBA)](Create_Sketch_Line_with_Visual_Properties_Example_VB.htm)
[Get Temporary Axes in Each Drawing View (VBA)](Get_Temporary_Axes_in_Each_Drawing_View_Example_VB.htm)

## Remarks

This property is only supported in drawing documents.

Sketch segments can be created on a layer that has specific visual properties. By default, the sketch segment takes on the visual properties defined by the layer. The line width value specified with this property overrides the default layer width.

Use the [ISketchSegment::LayerOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~LayerOverride.html) to determine if this sketch segment is currently using its default layer line width.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::Color Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Color.html)
[ISketchSegment::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Layer.html)
[ISketchSegment::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Style.html)

## Availability

SOLIDWORKS 99, datecode 1999207
