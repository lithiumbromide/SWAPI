---
title: "Width Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "Width"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Width.html"
---

# Width Property (IAnnotation)

Gets or sets the line width enumeration value for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
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

Line style as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

## VBA Syntax

See [Annotation::Width](ms-its:sldworksapivb6.chm::/sldworks~Annotation~Width.html).

## Remarks

Annotation width is currently supported only in SOLIDWORKS drawings.

In drawing documents, you can create annotations on a layer that has specific visual properties. By default, the annotation takes on the visual properties defined by the layer. The line width value specified with this property allows you to override the default layer width.

Use the [IAnnotation::LayerOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~LayerOverride.html) to determine if this annotation is using its default layer line width.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
