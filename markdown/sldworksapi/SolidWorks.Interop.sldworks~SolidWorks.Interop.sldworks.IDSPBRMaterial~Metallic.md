---
title: "Metallic Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Metallic"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Metallic.html"
---

# Metallic Property (IDSPBRMaterial)

Gets or sets the metallic-ness of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property Metallic As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.Metallic = value

value = instance.Metallic
```

### C#

```csharp
System.double Metallic {get; set;}
```

### C++/CLI

```cpp
property System.double Metallic {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (dielectric) default <= Metallic-ness value <= 1.0 (metallic)

## VBA Syntax

See [DSPBRMaterial::Metallic](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Metallic.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Metallic" in the pop up. Click **Next result** repeatedly.

- Search for "Metallic vs metal" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
