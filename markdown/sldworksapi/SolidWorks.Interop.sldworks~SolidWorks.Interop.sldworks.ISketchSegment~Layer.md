---
title: "Layer Property (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "Layer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Layer.html"
---

# Layer Property (ISketchSegment)

gets or sets the layer used by this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
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

Name of the layer used for this sketch segment

## VBA Syntax

See [SketchSegment::Layer](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~Layer.html).

## Remarks

Layers are only supported in drawing documents.

Sketch segments can be created on a specific layer. This property gets or sets the layer used by this sketch segment.

The return value may be an empty string because an old document may not contain layers. This also occurs if sketch segments have been generated in a new document that has no layers defined.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::LayerOverride Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~LayerOverride.html)
[ISketchSegment::Color Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Color.html)
[ISketchSegment::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Style.html)
[ISketchSegment::Width Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Width.html)

## Availability

SOLIDWORKS 99, datecode 1999207
