---
title: "Angle Property (ITexture)"
project: "SOLIDWORKS API Help"
interface: "ITexture"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~Angle.html"
---

# Angle Property (ITexture)

Gets or sets the rotation angle of the texture.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITexture
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 < Angle in degrees of texture rotation < 360.0

## VBA Syntax

See [Texture::Angle](ms-its:sldworksapivb6.chm::/sldworks~Texture~Angle.html).

## Examples

See the [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html) examples.

## See Also

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
