---
title: "Clearcoat Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Clearcoat"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Clearcoat.html"
---

# Clearcoat Property (IDSPBRMaterial)

Gets or sets the clearcoat reflectivity of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property Clearcoat As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.Clearcoat = value

value = instance.Clearcoat
```

### C#

```csharp
System.double Clearcoat {get; set;}
```

### C++/CLI

```cpp
property System.double Clearcoat {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) <= Clearcoat reflectivity < = 1.0

## VBA Syntax

See [DSPBRMaterial::Clearcoat](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Clearcoat.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Clearcoat" in the pop up. Click **Next result** repeatedly.

- Search for "clearcoat" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
