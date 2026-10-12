---
title: "DecalType Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "DecalType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~DecalType.html"
---

# DecalType Property (ITexture)

Gets whether the texture is a decal.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DecalType As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Boolean

value = instance.DecalType
```

### C#

```csharp
System.bool DecalType {get;}
```

### C++/CLI

```cpp
property System.bool DecalType {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the texture is a decal, false if not

## VBA Syntax

See [Texture::DecalType](ms-its:sldworksapivb6.chm::/sldworks~Texture~DecalType.html).

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
