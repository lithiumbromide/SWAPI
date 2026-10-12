---
title: "VDir Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "VDir"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~VDir.html"
---

# VDir Property (ITexture)

Gets the V value of the texture-based appearance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VDir As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Double

value = instance.VDir
```

### C#

```csharp
System.double VDir {get;}
```

### C++/CLI

```cpp
property System.double VDir {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

V value of the texture-based appearance

## VBA Syntax

See [Texture::VDir](ms-its:sldworksapivb6.chm::/sldworks~Texture~VDir.html).

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)
[ITexture::UDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~UDir.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
