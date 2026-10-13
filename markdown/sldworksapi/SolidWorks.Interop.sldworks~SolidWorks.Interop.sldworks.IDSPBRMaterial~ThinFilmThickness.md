---
title: "ThinFilmThickness Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "ThinFilmThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinFilmThickness.html"
---

# ThinFilmThickness Property (IDSPBRMaterial)

Gets or sets the thin film layer thickness for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinFilmThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.ThinFilmThickness = value

value = instance.ThinFilmThickness
```

### C#

```csharp
System.double ThinFilmThickness {get; set;}
```

### C++/CLI

```cpp
property System.double ThinFilmThickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Thin film layer thickness in microns <= 1.0; 0.4 is the default

## VBA Syntax

See [DSPBRMaterial::ThinFilmThickness](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~ThinFilmThickness.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Thickness of the thin-film layer" in the pop up. Click **Next result** repeatedly.

- Search for "Thin films" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
