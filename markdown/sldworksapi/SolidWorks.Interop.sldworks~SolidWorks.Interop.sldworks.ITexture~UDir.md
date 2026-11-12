---
title: "UDir Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "UDir"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~UDir.html"
---

# UDir Property (ITexture)

Gets the U value of the texture-based appearance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UDir As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Double

value = instance.UDir
```

### C#

```csharp
System.double UDir {get;}
```

### C++/CLI

```cpp
property System.double UDir {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

U value of the texture-based appearance

## VBA Syntax

See [Texture::UDir](ms-its:sldworksapivb6.chm::/sldworks~Texture~UDir.html).

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)
[ITexture::VDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~VDir.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
