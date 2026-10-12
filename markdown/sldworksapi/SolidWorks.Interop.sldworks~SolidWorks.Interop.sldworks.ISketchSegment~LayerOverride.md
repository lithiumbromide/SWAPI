---
title: "LayerOverride Property (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "LayerOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~LayerOverride.html"
---

# LayerOverride Property (ISketchSegment)

Gets or sets whether the sketch segment has properties that override the default properties of the layer.

## Syntax

### Visual Basic (Declaration)

```vb
Property LayerOverride As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Integer

instance.LayerOverride = value

value = instance.LayerOverride
```

### C#

```csharp
System.int LayerOverride {get; set;}
```

### C++/CLI

```cpp
property System.int LayerOverride {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Properties that have been overridden or should be overridden as defined in [swLayerOverride_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLayerOverride_e.html) (see Remarks)

## VBA Syntax

See [SketchSegment::LayerOverride](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~LayerOverride.html).

## Remarks

Layers are only supported in drawing documents.

Sketch segments can be created on a layer that has specific visual properties. By default, the sketch segment takes on the visual properties defined by the layer. However, for a specific sketch segment, these visual properties can be overridden (see [ISketchSegment::Color](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Color.html), [ISketchSegment::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Style.html), and [ISketchSegment::Width](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Width.html)). This property gets or sets whether the default visual properties of the layer are used by this sketch segment.

When the sketch segment is not on any layer, the value this property returns is undefined. You can use the [ISketchSegment::Layer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Layer.html) property to determine the name of the layer, if any, that this sketch segment is on. If an empty string is returned by the ISketchSegment::Layer property, then this property is not used.

If getting properties that override the default properties of the layer, the returned bit value indicates which properties have been overridden. The bit indicators are:

- color = 0x1
- style = 0x2
- width = 0x4

Therefore, if the return value is 3, then you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

If setting properties that override the default properties of the layer, the input bit value indicates which properties should maintain their current override values. The bit indicators are:

- color = 0x1
- style = 0x2
- width = 0x4

Therefore, if the value is passed is 0x4, then you know the width should keep its current override value and that the color and style visual properties for this sketch segment should be reset to use the color and style settings of the item's layer. If you pass 0, then all visual properties are reset to use the default settings of the item's layer.

Only set this to reset specific visual properties back to the default visual properties of the owning layer. If you want to change or set specific values for the visual property for this item, use [ISketchSegment::Color](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Color.html), [ISketchSegment::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Style.html), and [ISketchSegment::Width](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Width.html).

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
