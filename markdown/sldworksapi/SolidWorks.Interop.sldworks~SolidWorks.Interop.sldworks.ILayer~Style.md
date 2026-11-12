---
title: "Style Property (ILayer)"
project: "SOLIDWORKS API Help"
interface: "ILayer"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Style.html"
---

# Style Property (ILayer)

Gets and sets the line style for this layer.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILayer
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

See [Layer::Style](ms-its:sldworksapivb6.chm::/sldworks~Layer~Style.html).

## Examples

[Get Layers (C#)](Get_Layers_Example_CSharp.htm)
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## See Also

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.html)
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.html)
[ILayer::Width Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Width.html)

## Availability

SOLIDWORKS 99, datecode 1999207
