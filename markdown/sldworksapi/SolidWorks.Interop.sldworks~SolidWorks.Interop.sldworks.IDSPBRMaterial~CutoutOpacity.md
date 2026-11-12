---
title: "CutoutOpacity Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "CutoutOpacity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~CutoutOpacity.html"
---

# CutoutOpacity Property (IDSPBRMaterial)

Gets or sets the cut-out opacity of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property CutoutOpacity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.CutoutOpacity = value

value = instance.CutoutOpacity
```

### C#

```csharp
System.double CutoutOpacity {get; set;}
```

### C++/CLI

```cpp
property System.double CutoutOpacity {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (transparent) <= Cut-out opacity <= 1.0 (opaque) default

## VBA Syntax

See [DSPBRMaterial::CutoutOpacity](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~CutoutOpacity.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Cut-out opacity" in the pop up. Click **Next result** repeatedly.

- Search for "cut-out opacity" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
