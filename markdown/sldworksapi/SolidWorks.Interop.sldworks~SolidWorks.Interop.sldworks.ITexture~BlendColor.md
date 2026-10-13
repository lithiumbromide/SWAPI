---
title: "BlendColor Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "BlendColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~BlendColor.html"
---

# BlendColor Property (ITexture)

Gets or sets whether to blend the part color with the texture color.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlendColor As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Boolean

instance.BlendColor = value

value = instance.BlendColor
```

### C#

```csharp
System.bool BlendColor {get; set;}
```

### C++/CLI

```cpp
property System.bool BlendColor {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to blend the colors of the part and texture, false to not

## VBA Syntax

See [Texture::BlendColor](ms-its:sldworksapivb6.chm::/sldworks~Texture~BlendColor.html).

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
