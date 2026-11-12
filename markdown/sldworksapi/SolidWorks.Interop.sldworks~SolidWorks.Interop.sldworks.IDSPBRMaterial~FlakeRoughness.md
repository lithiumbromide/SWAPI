---
title: "FlakeRoughness Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "FlakeRoughness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlakeRoughness.html"
---

# FlakeRoughness Property (IDSPBRMaterial)

Gets or sets the roughness of distribution that controls flake orientation in this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlakeRoughness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.FlakeRoughness = value

value = instance.FlakeRoughness
```

### C#

```csharp
System.double FlakeRoughness {get; set;}
```

### C++/CLI

```cpp
property System.double FlakeRoughness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) <= Flake roughness <= 1.0

## VBA Syntax

See [DSPBRMaterial::FlakeRoughness](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~FlakeRoughness.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Flake" in the pop up. Click **Next result** repeatedly.

- Search for "flake roughness in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
