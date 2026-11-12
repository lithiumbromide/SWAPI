---
title: "EmissionMode Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "EmissionMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionMode.html"
---

# EmissionMode Property (IDSPBRMaterial)

Gets or sets the emission mode for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property EmissionMode As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Integer

instance.EmissionMode = value

value = instance.EmissionMode
```

### C#

```csharp
System.int EmissionMode {get; set;}
```

### C++/CLI

```cpp
property System.int EmissionMode {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 = luminous emittance (default) or 1 = luminous power

## VBA Syntax

See [DSPBRMaterial::EmissionMode](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~EmissionMode.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Emission mode" in the pop up. Click **Next result** repeatedly.

- Search for "emission mode" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
