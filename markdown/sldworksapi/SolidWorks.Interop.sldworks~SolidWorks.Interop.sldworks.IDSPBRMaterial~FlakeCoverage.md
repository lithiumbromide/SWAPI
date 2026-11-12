---
title: "FlakeCoverage Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "FlakeCoverage"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlakeCoverage.html"
---

# FlakeCoverage Property (IDSPBRMaterial)

Gets or sets the flake coverage of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlakeCoverage As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.FlakeCoverage = value

value = instance.FlakeCoverage
```

### C#

```csharp
System.double FlakeCoverage {get; set;}
```

### C++/CLI

```cpp
property System.double FlakeCoverage {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (no flakes) default <= Flake coverage <= 1.0 (only flakes)

## VBA Syntax

See [DSPBRMaterial::FlakeCoverage](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~FlakeCoverage.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Flake coverage" in the pop up. Click **Next result** repeatedly.

- Search for "flake coverage in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
