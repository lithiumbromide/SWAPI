---
title: "ClearcoatRoughness Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "ClearcoatRoughness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ClearcoatRoughness.html"
---

# ClearcoatRoughness Property (IDSPBRMaterial)

Gets or sets the roughness of clearcoat's microfacet distribution in this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClearcoatRoughness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.ClearcoatRoughness = value

value = instance.ClearcoatRoughness
```

### C#

```csharp
System.double ClearcoatRoughness {get; set;}
```

### C++/CLI

```cpp
property System.double ClearcoatRoughness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) <= Clear coat roughness value <= 1.0

## VBA Syntax

See [DSPBRMaterial::ClearcoatRoughness](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~ClearcoatRoughness.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Clearcoat" in the pop up. Click **Next result** repeatedly.

- Search for "clearcoat roughness" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
