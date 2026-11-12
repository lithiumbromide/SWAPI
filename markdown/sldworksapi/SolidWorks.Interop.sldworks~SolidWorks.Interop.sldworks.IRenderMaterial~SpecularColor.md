---
title: "SpecularColor Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SpecularColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SpecularColor.html"
---

# SpecularColor Property (IRenderMaterial)

Gets or sets the specular color for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpecularColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.SpecularColor = value

value = instance.SpecularColor
```

### C#

```csharp
System.int SpecularColor {get; set;}
```

### C++/CLI

```cpp
property System.int SpecularColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB value

## VBA Syntax

See [RenderMaterial::SpecularColor](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~SpecularColor.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
