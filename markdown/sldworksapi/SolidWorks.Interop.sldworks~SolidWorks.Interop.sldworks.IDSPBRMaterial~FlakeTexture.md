---
title: "FlakeTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "FlakeTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~FlakeTexture.html"
---

# FlakeTexture Property (IDSPBRMaterial)

Gets or sets the flake texture map of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlakeTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.FlakeTexture = value

value = instance.FlakeTexture
```

### C#

```csharp
System.string FlakeTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ FlakeTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Flake texture map

## VBA Syntax

See [DSPBRMaterial::FlakeTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~FlakeTexture.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Flake texture" in the pop up. Click **Next result** repeatedly.

- Search for "flake texture in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
