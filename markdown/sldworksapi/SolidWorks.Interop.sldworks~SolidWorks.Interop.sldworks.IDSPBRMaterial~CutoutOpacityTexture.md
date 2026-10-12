---
title: "CutoutOpacityTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "CutoutOpacityTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~CutoutOpacityTexture.html"
---

# CutoutOpacityTexture Property (IDSPBRMaterial)

Gets or sets the cut-out opacity texture map of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property CutoutOpacityTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.CutoutOpacityTexture = value

value = instance.CutoutOpacityTexture
```

### C#

```csharp
System.string CutoutOpacityTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ CutoutOpacityTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the cut-out opacity texture map

## VBA Syntax

See [DSPBRMaterial::CutoutOpacityTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~CutoutOpacityTexture.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Cut-out texture" in the pop up. Click **Next result** repeatedly.
- Search for "cut-out opacity texture map" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
