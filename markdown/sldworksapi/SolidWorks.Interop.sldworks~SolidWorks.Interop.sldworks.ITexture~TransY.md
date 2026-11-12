---
title: "TransY Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "TransY"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~TransY.html"
---

# TransY Property (ITexture)

Gets the y coordinate for the translation point of the texture-based appearance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TransY As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Double

value = instance.TransY
```

### C#

```csharp
System.double TransY {get;}
```

### C++/CLI

```cpp
property System.double TransY {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

y coordinate for the translation point of the texture-based appearance

## VBA Syntax

See [Texture::TransY](ms-its:sldworksapivb6.chm::/sldworks~Texture~TransY.html).

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)
[ITexture::TransX Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~TransX.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
