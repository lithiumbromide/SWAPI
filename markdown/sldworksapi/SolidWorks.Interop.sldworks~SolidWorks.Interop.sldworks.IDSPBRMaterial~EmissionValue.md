---
title: "EmissionValue Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "EmissionValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionValue.html"
---

# EmissionValue Property (IDSPBRMaterial)

Gets or sets the amount of light projected from this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property EmissionValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.EmissionValue = value

value = instance.EmissionValue
```

### C#

```csharp
System.double EmissionValue {get; set;}
```

### C++/CLI

```cpp
property System.double EmissionValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) <= Emission (w/srm^2) < 500.0

## VBA Syntax

See [DSPBRMaterial::EmissionValue](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~EmissionValue.html).

## Remarks

The [IDSPBRMaterial::EmissionMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionMode.html) determines the units of this property's value.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Emission value" in the pop up. Click **Next result** repeatedly.

- Search for "emissivity in materials" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
