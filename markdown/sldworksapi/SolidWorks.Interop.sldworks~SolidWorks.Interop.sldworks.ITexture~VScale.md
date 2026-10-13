---
title: "VScale Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "VScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~VScale.html"
---

# VScale Property (ITexture)

Gets the scale for this texture-based appearance or decal.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Double

value = instance.VScale
```

### C#

```csharp
System.double VScale {get;}
```

### C++/CLI

```cpp
property System.double VScale {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Scale

## VBA Syntax

See [Texture::VScale](ms-its:sldworksapivb6.chm::/sldworks~Texture~VScale.html).

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
