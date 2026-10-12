---
title: "AnisotropyRotation Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "AnisotropyRotation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~AnisotropyRotation.html"
---

# AnisotropyRotation Property (IDSPBRMaterial)

Gets or sets the anisotropy rotation angle (counter-clockwise rotation of the tangent space around local normal).

## Syntax

### Visual Basic (Declaration)

```vb
Property AnisotropyRotation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.AnisotropyRotation = value

value = instance.AnisotropyRotation
```

### C#

```csharp
System.double AnisotropyRotation {get; set;}
```

### C++/CLI

```cpp
property System.double AnisotropyRotation {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (0 degrees) default <= Anisotropy rotation value <= 1.0 (360 degrees)

## VBA Syntax

See [DSPBRMaterial::AnisotropyRotation](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~AnisotropyRotation.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Anisotropy rotation" in the pop up. Click **Next result** repeatedly.

- Search for "Anisotropy rotation values of materials" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
