---
title: "Layer Property (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "Layer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Layer.html"
---

# Layer Property (ISketchHatch)

Gets or sets the layer used by this sketch hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
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

Name of the layer for this sketch hatch

## VBA Syntax

See [SketchHatch::Layer](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~Layer.html).

## Examples

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html) examples.

## Examples

[Override Layer Color for Area Hatch (VBA)](Override_Layer_Color_for_Area_Hatch_Example_VB.htm)

## Remarks

In drawing documents, sketch hatches can be created on a specific layer. Only drawing documents support layers.

The return value can be an empty string because an old document may not contain layers. This can also occur if sketch hatches have been generated in a new document in which layers have not been defined.

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
[ISketchHatch::LayerOverride Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~LayerOverride.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
