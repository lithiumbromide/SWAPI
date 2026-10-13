---
title: "TransX Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "TransX"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~TransX.html"
---

# TransX Property (ITexture)

Gets the x coordinate for the translation point of the texture-based appearance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TransX As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Double

value = instance.TransX
```

### C#

```csharp
System.double TransX {get;}
```

### C++/CLI

```cpp
property System.double TransX {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

x coordinate for the translation point of the texture-based appearance

## VBA Syntax

See [Texture::TransX](ms-its:sldworksapivb6.chm::/sldworks~Texture~TransX.html).

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)
[ITexture::TransY Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~TransY.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
