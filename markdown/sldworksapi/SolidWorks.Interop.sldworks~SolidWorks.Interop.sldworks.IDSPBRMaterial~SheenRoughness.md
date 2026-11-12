---
title: "SheenRoughness Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "SheenRoughness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SheenRoughness.html"
---

# SheenRoughness Property (IDSPBRMaterial)

Gets or sets the roughness of sheen microfacet distribution for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheenRoughness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.SheenRoughness = value

value = instance.SheenRoughness
```

### C#

```csharp
System.double SheenRoughness {get; set;}
```

### C++/CLI

```cpp
property System.double SheenRoughness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Sheen roughness <= 1.0; 0.5 is the default

## VBA Syntax

See [DSPBRMaterial::SheenRoughness](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~SheenRoughness.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Sheen" in the pop up. Click **Next result** repeatedly.

- Search for "Sheen roughness in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
