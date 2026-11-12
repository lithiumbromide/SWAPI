---
title: "Color Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "Color"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Color.html"
---

# Color Property (IAnnotation)

Gets or sets the color of this annotation. Annotation color is supported only in SOLIDWORKS drawings.

## Syntax

### Visual Basic (Declaration)

```vb
Property Color As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
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

COLORREF value for the color of this annotation

## VBA Syntax

See [Annotation::Color](ms-its:sldworksapivb6.chm::/sldworks~Annotation~Color.html).

## Remarks

In Drawing documents, you can create annotations on a layer that has specific visual properties. The color value specified with this property overrides the layer color.

Use [IAnnotation::LayerOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~LayerOverride.html) to determine whether this annotation is using its default layer color.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
