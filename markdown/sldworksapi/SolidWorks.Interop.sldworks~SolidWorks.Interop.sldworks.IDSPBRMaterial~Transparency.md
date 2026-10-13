---
title: "Transparency Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "Transparency"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~Transparency.html"
---

# Transparency Property (IDSPBRMaterial)

Gets or sets the degree to which this material allows light to pass through for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Transparency As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.Transparency = value

value = instance.Transparency
```

### C#

```csharp
System.double Transparency {get; set;}
```

### C++/CLI

```cpp
property System.double Transparency {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (opaque) default <= Transparency <= 1.0 (translucent)

## VBA Syntax

See [DSPBRMaterial::Transparency](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~Transparency.html).

## Remarks

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Transparency" in the pop up. Click **Next result** repeatedly.

- Search for "Transparency in materials science" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
