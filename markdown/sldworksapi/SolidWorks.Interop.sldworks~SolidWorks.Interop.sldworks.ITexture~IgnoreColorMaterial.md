---
title: "IgnoreColorMaterial Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "IgnoreColorMaterial"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~IgnoreColorMaterial.html"
---

# IgnoreColorMaterial Property (ITexture)

Gets whether to ignore the color texture-based appearance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IgnoreColorMaterial As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Boolean

value = instance.IgnoreColorMaterial
```

### C#

```csharp
System.bool IgnoreColorMaterial {get;}
```

### C++/CLI

```cpp
property System.bool IgnoreColorMaterial {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to ignore the color of this texture-based appearance, false to not

## VBA Syntax

See [Texture::IgnoreColorMaterial](ms-its:sldworksapivb6.chm::/sldworks~Texture~IgnoreColorMaterial.html).

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
