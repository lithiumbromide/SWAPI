---
title: "AbbeNumber Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "AbbeNumber"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~AbbeNumber.html"
---

# AbbeNumber Property (IDSPBRMaterial)

Gets or sets the dispersion of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property AbbeNumber As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.AbbeNumber = value

value = instance.AbbeNumber
```

### C#

```csharp
System.double AbbeNumber {get; set;}
```

### C++/CLI

```cpp
property System.double AbbeNumber {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) <= Abbe number < 500.0

## VBA Syntax

See [DSPBRMaterial::AbbeNumber](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~AbbeNumber.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Abbe number" in the pop up. Click **Next result** repeatedly.

- Search for "Abbe number" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
