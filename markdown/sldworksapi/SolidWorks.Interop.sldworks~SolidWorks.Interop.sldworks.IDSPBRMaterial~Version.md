---
title: "Version Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Version"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Version.html"
---

# Version Property (IDSPBRMaterial)

Gets or sets the version of the model specification used for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property Version As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.Version = value

value = instance.Version
```

### C#

```csharp
System.string Version {get; set;}
```

### C++/CLI

```cpp
property System.String^ Version {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Version 2025x

## VBA Syntax

See [DSPBRMaterial::Version](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Version.html).

## Remarks

For more information about versions of the DSPBR Shading Model, open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Changelog" in the pop up. Click **Next result** repeatedly.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
