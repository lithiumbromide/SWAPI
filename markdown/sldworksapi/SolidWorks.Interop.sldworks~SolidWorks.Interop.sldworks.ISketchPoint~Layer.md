---
title: "Layer Property (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "Layer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Layer.html"
---

# Layer Property (ISketchPoint)

Gets or sets the layer for this sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
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

Name of the layer for this sketch point

## VBA Syntax

See [SketchPoint::Layer](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~Layer.html).

## Remarks

Layers are only supported in drawing documents.

Every sketch point is on a layer. Sketch points can be created on a specific layer in drawings.

The return value may be an empty string because an older document may not contain layers. Also, this can occur if sketch points were generated in a new document that has no layers defined.

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::LayerOverride Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~LayerOverride.html)

## Availability

SOLIDWORKS 99, datecode 1999207
