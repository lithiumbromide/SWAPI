---
title: "Anisotropy Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Anisotropy"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Anisotropy.html"
---

# Anisotropy Property (IDSPBRMaterial)

Gets or sets the anisotropy strength of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property Anisotropy As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.Anisotropy = value

value = instance.Anisotropy
```

### C#

```csharp
System.double Anisotropy {get; set;}
```

### C++/CLI

```cpp
property System.double Anisotropy {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) <= Anisotropy strength <= 1.0

## VBA Syntax

See [DSPBRMaterial::Anisotropy](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Anisotropy.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Anisotropy" in the pop up. Click **Next result** repeatedly.

- Search for "Anisotropy strength" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
