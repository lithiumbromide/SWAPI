---
title: "ScaleFactor Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "ScaleFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~ScaleFactor.html"
---

# ScaleFactor Property (ITexture)

Gets or sets the granularity of the texture.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Double

instance.ScaleFactor = value

value = instance.ScaleFactor
```

### C#

```csharp
System.double ScaleFactor {get; set;}
```

### C++/CLI

```cpp
property System.double ScaleFactor {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.001 < Granularity of the texture < 1000000.00

## VBA Syntax

See [Texture::ScaleFactor](ms-its:sldworksapivb6.chm::/sldworks~Texture~ScaleFactor.html).

## Examples

See the [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html) examples.

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
