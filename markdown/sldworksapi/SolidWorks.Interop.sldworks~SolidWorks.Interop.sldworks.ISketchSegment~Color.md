---
title: "Color Property (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "Color"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Color.html"
---

# Color Property (ISketchSegment)

Gets or sets the color of this sketch segment. Sketch segment color is only supported in drawing documents.

## Syntax

### Visual Basic (Declaration)

```vb
Property Color As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Integer

instance.Color = value

value = instance.Color
```

### C#

```csharp
System.int Color {get; set;}
```

### C++/CLI

```cpp
property System.int Color {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

COLORREF value for this sketch segment

## VBA Syntax

See [SketchSegment::Color](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~Color.html).

## Examples

[Get Temporary Axes in Each Drawing View (VBA)](Get_Temporary_Axes_in_Each_Drawing_View_Example_VB.htm)

## Remarks

Sketch segment color is only supported in drawing documents.

In drawing documents, sketch segments can be created on a layer that has specific visual properties. The color value specified with this property overrides the layer color.

Use the [ISketchSegment::LayerOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~LayerOverride.html) to determine if this sketch segment is currently using its default layer color.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Layer.html)
[ISketchSegment::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Style.html)
[ISketchSegment::Width Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Width.html)

## Availability

SOLIDWORKS 99, datecode 1999207
