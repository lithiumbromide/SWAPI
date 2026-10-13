---
title: "Translucency Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Translucency"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Translucency.html"
---

# Translucency Property (IDSPBRMaterial)

Gets or sets the degree to which this material is able to filter and diffuse light for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Translucency As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.Translucency = value

value = instance.Translucency
```

### C#

```csharp
System.double Translucency {get; set;}
```

### C++/CLI

```cpp
property System.double Translucency {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (opaque) default <= Translucency <= 1.0 (translucent)

## VBA Syntax

See [DSPBRMaterial::Translucency](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Translucency.html).

## Remarks

Increasing translucency gives the material more backlighting.

A light must be behind the model relative to the position of the viewer.

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Translucency" in the pop up. Click **Next result** repeatedly.

- Search for "Translucency in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
