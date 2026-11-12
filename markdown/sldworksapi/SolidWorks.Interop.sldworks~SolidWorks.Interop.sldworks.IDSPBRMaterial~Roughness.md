---
title: "Roughness Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Roughness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Roughness.html"
---

# Roughness Property (IDSPBRMaterial)

Gets or sets the specular spread (roughness) of the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Roughness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.Roughness = value

value = instance.Roughness
```

### C#

```csharp
System.double Roughness {get; set;}
```

### C++/CLI

```cpp
property System.double Roughness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) <= Specular spread <= 1.0

## VBA Syntax

See [DSPBRMaterial::Roughness](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Roughness.html).

## Remarks

This property controls the size of any highlights on a surface. It is also known as the specular exponent. Increasing roughness makes highlights larger and softer.

The [specular](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Specular.html) value must not be zero, the [specular tint color](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SpecularTintColor.html) must not be black, and at least one light other than an ambient light must be illuminating the model.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Roughness" in the pop up. Click **Next result** repeatedly.

- Search for "roughness in materials" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
