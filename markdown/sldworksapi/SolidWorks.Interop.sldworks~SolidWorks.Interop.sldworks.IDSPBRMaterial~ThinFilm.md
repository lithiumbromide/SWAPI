---
title: "ThinFilm Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "ThinFilm"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinFilm.html"
---

# ThinFilm Property (IDSPBRMaterial)

Gets or sets the thin film layer weight for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinFilm As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.ThinFilm = value

value = instance.ThinFilm
```

### C#

```csharp
System.double ThinFilm {get; set;}
```

### C++/CLI

```cpp
property System.double ThinFilm {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) <= Thin film layer weight <= 1.0

## VBA Syntax

See [DSPBRMaterial::ThinFilm](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~ThinFilm.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Thin film" in the pop up. Click **Next result** repeatedly.

- Search for "Thin films" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
