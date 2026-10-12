---
title: "LayerOverride Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "LayerOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LayerOverride.html"
---

# LayerOverride Property (IAnnotation)

Gets or sets whether the annotation has properties that override the default properties of the layer.

## Syntax

### Visual Basic (Declaration)

```vb
Property LayerOverride As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
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

See [Annotation::LayerOverride](ms-its:sldworksapivb6.chm::/sldworks~Annotation~LayerOverride.html).

## Remarks

Layers are currently supported only in SOLIDWORKS drawings.

You should set this property only when you want to reset specific visual properties to the default visual properties of the owning layer. If you want to change or set specific values for the visual property of this item, use [IAnnotation::Color](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Color.html), [IAnnotation::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Style.html), and [IAnnotation::Width](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Width.html).

In drawing documents, annotations can be created on a layer that has specific visual properties. By default, the annotation takes on the visual properties defined by the layer. However, for a specific annotation, you can override these visual properties (color, style, and width).

When the annotation is not on any layer, this property returns an undefined value. You can use the [IAnnotation::Layer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Layer.html) property to determine the name of the layer that this annotation is on. If an empty string is returned by the Annotation::Layer property, then this property is not used.

When you get this property, the returned bit value indicates which property or properties have been overridden. The bit indicators are:

Therefore, if the value was returned as 3, you know color and style have been specifically set for this item and might not match the default values associated with this item's layer.

When you set this property, the input bit value indicates which property or properties should maintain their current override values. Therefore, if the value is passed as 0x4, we know width should keep its current override value, and that color and style should be reset to use the color and style settings for the item's layer. If you pass 0, all visual properties are reset to use the default settings of the item's layer.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
