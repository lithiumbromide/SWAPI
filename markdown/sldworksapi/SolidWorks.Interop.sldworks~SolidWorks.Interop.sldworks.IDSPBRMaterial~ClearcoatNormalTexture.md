---
title: "ClearcoatNormalTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "ClearcoatNormalTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ClearcoatNormalTexture.html"
---

# ClearcoatNormalTexture Property (IDSPBRMaterial)

Gets or sets the clear coat normal texture map of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClearcoatNormalTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.ClearcoatNormalTexture = value

value = instance.ClearcoatNormalTexture
```

### C#

```csharp
System.string ClearcoatNormalTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ ClearcoatNormalTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the clear coat normal texture map

## VBA Syntax

See [DSPBRMaterial::ClearcoatNormalTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~ClearcoatNormalTexture.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Clearcoat normal" in the pop up. Click **Next result** repeatedly.

- Search for "clearcoat normal texture" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
