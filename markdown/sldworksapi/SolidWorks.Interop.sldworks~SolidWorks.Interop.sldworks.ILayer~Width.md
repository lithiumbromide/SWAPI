---
title: "Width Property (ILayer)"
project: "SOLIDWORKS API Help"
interface: "ILayer"
member: "Width"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Width.html"
---

# Width Property (ILayer)

Gets and sets the line width for this layer.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILayer
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

Line width as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

## VBA Syntax

See [Layer::Width](ms-its:sldworksapivb6.chm::/sldworks~Layer~Width.html).

## Examples

[Get Layers (C#)](Get_Layers_Example_CSharp.htm)
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## See Also

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.html)
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.html)
[ILayer::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Style.html)

## Availability

SOLIDWORKS 99, datecode 1999207
