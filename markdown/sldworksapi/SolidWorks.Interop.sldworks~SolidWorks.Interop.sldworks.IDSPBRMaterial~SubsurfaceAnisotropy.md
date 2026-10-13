---
title: "SubsurfaceAnisotropy Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "SubsurfaceAnisotropy"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SubsurfaceAnisotropy.html"
---

# SubsurfaceAnisotropy Property (IDSPBRMaterial)

Gets or sets the subsurface scattering anisotropy value for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property SubsurfaceAnisotropy As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.SubsurfaceAnisotropy = value

value = instance.SubsurfaceAnisotropy
```

### C#

```csharp
System.double SubsurfaceAnisotropy {get; set;}
```

### C++/CLI

```cpp
property System.double SubsurfaceAnisotropy {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- 1.0 (backward scattering) <= Subsurface scattering anisotropy value <= 1.0 (forward scattering)

## VBA Syntax

See [DSPBRMaterial::SubsurfaceAnisotropy](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~SubsurfaceAnisotropy.html).

## Remarks

The default value of this property is 0.0 for isotropic scattering.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Subsurface anisotropy" in the pop up. Click **Next result** repeatedly.

- Search for "Subsurface scattering anisotropy in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
