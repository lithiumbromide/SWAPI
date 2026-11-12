---
title: "RealViewToDSPBRTextureScale Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "RealViewToDSPBRTextureScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~RealViewToDSPBRTextureScale.html"
---

# RealViewToDSPBRTextureScale Property (IDSPBRMaterial)

Gets or sets the RealView to DSPBR texture map scale for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property RealViewToDSPBRTextureScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.RealViewToDSPBRTextureScale = value

value = instance.RealViewToDSPBRTextureScale
```

### C#

```csharp
System.double RealViewToDSPBRTextureScale {get; set;}
```

### C++/CLI

```cpp
property System.double RealViewToDSPBRTextureScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RealView to DSPBR texture map scale

## VBA Syntax

See [DSPBRMaterial::RealViewToDSPBRTextureScale](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~RealViewToDSPBRTextureScale.html).

## Remarks

Search for "RealView texture map scale" on the web to obtain more information about this property.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
