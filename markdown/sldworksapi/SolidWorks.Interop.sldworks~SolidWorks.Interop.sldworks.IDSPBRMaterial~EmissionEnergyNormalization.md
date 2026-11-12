---
title: "EmissionEnergyNormalization Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "EmissionEnergyNormalization"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionEnergyNormalization.html"
---

# EmissionEnergyNormalization Property (IDSPBRMaterial)

Gets or sets the emission energy normalization value for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property EmissionEnergyNormalization As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Integer

instance.EmissionEnergyNormalization = value

value = instance.EmissionEnergyNormalization
```

### C#

```csharp
System.int EmissionEnergyNormalization {get; set;}
```

### C++/CLI

```cpp
property System.int EmissionEnergyNormalization {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True (1) to enable emission energy normalization, default false (0) to not

## VBA Syntax

See [DSPBRMaterial::EmissionEnergyNormalization](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~EmissionEnergyNormalization.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Normalize emission color" in the pop up. Click **Next result** repeatedly.
- Search for "Emission energy normalization in materials" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
