---
title: "ThinWalled Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "ThinWalled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinWalled.html"
---

# ThinWalled Property (IDSPBRMaterial)

Gets or sets whether this material is thin walled.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinWalled As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Integer

instance.ThinWalled = value

value = instance.ThinWalled
```

### C#

```csharp
System.int ThinWalled {get; set;}
```

### C++/CLI

```cpp
property System.int ThinWalled {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True (1) if thin walled (default), false (0) if material describes volume boundary

## VBA Syntax

See [DSPBRMaterial::ThinWalled](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~ThinWalled.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Thin-walled" in the pop up. Click **Next result** repeatedly.

- Search for "Thin walled value in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
