---
title: "AttenuationDistance Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "AttenuationDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~AttenuationDistance.html"
---

# AttenuationDistance Property (IDSPBRMaterial)

Gets or sets the distance of attenuation in this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property AttenuationDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.AttenuationDistance = value

value = instance.AttenuationDistance
```

### C#

```csharp
System.double AttenuationDistance {get; set;}
```

### C++/CLI

```cpp
property System.double AttenuationDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Distance of attenuation < 500000.0 (default)

## VBA Syntax

See [DSPBRMaterial::AttenuationDistance](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~AttenuationDistance.html).

## Remarks

If this property is 0.0, the surface is opaque.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Attenuation distance" in the pop up. Click **Next result** repeatedly.

- Search for "attenuation distance" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
