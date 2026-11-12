---
title: "IndexOfRefraction Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "IndexOfRefraction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~IndexOfRefraction.html"
---

# IndexOfRefraction Property (IDSPBRMaterial)

Gets or sets the index of refraction for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property IndexOfRefraction As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.IndexOfRefraction = value

value = instance.IndexOfRefraction
```

### C#

```csharp
System.double IndexOfRefraction {get; set;}
```

### C++/CLI

```cpp
property System.double IndexOfRefraction {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

1.0 <= Refractive index < 500.0; 1.5 is the default

## VBA Syntax

See [DSPBRMaterial::IndexOfRefraction](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~IndexOfRefraction.html).

## Remarks

This property controls the bending of light as it passes through a transparent object. Although actually dependent on the ratio of indices between the transparent material entered and the material exited, in practice, the higher the index of refraction, the more the light is bent. Typical values are 1.0 for air, 1.33 for water, and 1.44 for glass.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Index of refraction" in the pop up. Click **Next result** repeatedly.

- Search for "Refractive index" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
