---
title: "Style Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Style.html"
---

# Style Property (IAnnotation)

Gets or sets the line style for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

instance.Style = value

value = instance.Style
```

### C#

```csharp
System.int Style {get; set;}
```

### C++/CLI

```cpp
property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Line style as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

## VBA Syntax

See [Annotation::Style](ms-its:sldworksapivb6.chm::/sldworks~Annotation~Style.html).

## Remarks

Annotation style is currently supported only in SOLIDWORKS drawings.

In drawing documents, annotations can be created on a layer that has specific visual properties. By default, the annotation takes on the visual properties defined by the layer. The style value specified with this property allows you to override the default layer style.

Use [IAnnotation::LayerOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~LayerOverride.html) to determine whether or not this annotation is currently using its default layer line style.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
