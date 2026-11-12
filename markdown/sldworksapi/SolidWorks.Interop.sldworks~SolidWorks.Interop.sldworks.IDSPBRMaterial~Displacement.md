---
title: "Displacement Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Displacement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Displacement.html"
---

# Displacement Property (IDSPBRMaterial)

Gets or sets the displacement in the direction of the surface normal to add details to the geomtry of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property Displacement As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.Displacement = value

value = instance.Displacement
```

### C#

```csharp
System.double Displacement {get; set;}
```

### C++/CLI

```cpp
property System.double Displacement {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) < Displacement value (mm) < 500000.0

## VBA Syntax

See [DSPBRMaterial::Displacement](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Displacement.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Displacement" in the pop up. Click **Next result** repeatedly.

- Search for "displacement texture map" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
