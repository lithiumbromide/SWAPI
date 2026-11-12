---
title: "ThinFilmIOR Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "ThinFilmIOR"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinFilmIOR.html"
---

# ThinFilmIOR Property (IDSPBRMaterial)

Gets or sets the thin film layer index of refraction for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinFilmIOR As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.ThinFilmIOR = value

value = instance.ThinFilmIOR
```

### C#

```csharp
System.double ThinFilmIOR {get; set;}
```

### C++/CLI

```cpp
property System.double ThinFilmIOR {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

1.0 <= Thin film layer index of refraction <= 2.5; 1.3 is the default

## VBA Syntax

See [DSPBRMaterial::ThinFilmThicknessIOR](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~ThinFilmThicknessIOR.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Index of refraction of the thin-film layer" in the pop up. Click **Next result** repeatedly.
- Search for "Thin film index of refraction" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
