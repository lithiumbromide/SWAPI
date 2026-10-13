---
title: "ThinFilmThicknessTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "ThinFilmThicknessTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~ThinFilmThicknessTexture.html"
---

# ThinFilmThicknessTexture Property (IDSPBRMaterial)

Gets or sets the thin film layer thickness texture map for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinFilmThicknessTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.ThinFilmThicknessTexture = value

value = instance.ThinFilmThicknessTexture
```

### C#

```csharp
System.string ThinFilmThicknessTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ ThinFilmThicknessTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the thin film layer thickness texture map

## VBA Syntax

See [DSPBRMaterial::ThinFilmThicknessTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~ThinFilmThicknessTexture.html).

## Remarks

For more information about this property, search for "Thin film thickness texture map" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
