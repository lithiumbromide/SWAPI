---
title: "Layer Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "Layer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Layer.html"
---

# Layer Property (IAnnotation)

Gets or sets the layer used by this annotation. Layers are supported only in SOLIDWORKS
drawings.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.String

instance.Layer = value

value = instance.Layer
```

### C#

```csharp
System.string Layer {get; set;}
```

### C++/CLI

```cpp
property System.String^ Layer {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the layer used for this annotation

## VBA Syntax

See [Annotation::Layer](ms-its:sldworksapivb6.chm::/sldworks~Annotation~Layer.html).

## Examples

[Insert Autoballoons (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)

## Remarks

In Drawing documents, annotations can be created on a specific layer. This property allows you to get or set the layer used by this annotation. You can also set an annotation to not be on any layer by specifying "" for theLayer.

**NOTE:** The return value might be an empty string because an old document might not contain layers. This also occurs if annotations have been generated in a new document that does not have layers defined.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
