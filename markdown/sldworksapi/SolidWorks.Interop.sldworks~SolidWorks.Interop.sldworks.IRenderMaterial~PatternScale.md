---
title: "PatternScale Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "PatternScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~PatternScale.html"
---

# PatternScale Property (IRenderMaterial)

Gets or sets the pattern scale of procedural textures for mapping the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.PatternScale = value

value = instance.PatternScale
```

### C#

```csharp
System.double PatternScale {get; set;}
```

### C++/CLI

```cpp
property System.double PatternScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern scale

## VBA Syntax

See [RenderMaterial::PatternScale](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~PatternScale.html).

## Remarks

A procedural texture is one where you only have control over the colors in the material and the size of the material (for example, colored marble or cherry wood).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
