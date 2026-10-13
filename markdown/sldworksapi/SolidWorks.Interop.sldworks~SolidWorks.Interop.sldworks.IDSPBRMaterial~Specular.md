---
title: "Specular Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Specular"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Specular.html"
---

# Specular Property (IDSPBRMaterial)

Gets or sets the intensity of the light surface for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Specular As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.Specular = value

value = instance.Specular
```

### C#

```csharp
System.double Specular {get; set;}
```

### C++/CLI

```cpp
property System.double Specular {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Specular value <= 1.0 (default)

## VBA Syntax

See [DSPBRMaterial::Specular](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Specular.html).

## Remarks

This property depends on the position of the light source and the position of the viewer. Increasing specular makes the material appear shinier.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Specular" in the pop up. Click **Next result** repeatedly.

- Search for "Specular in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
