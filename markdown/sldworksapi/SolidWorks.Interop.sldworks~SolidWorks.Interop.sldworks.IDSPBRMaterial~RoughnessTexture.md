---
title: "RoughnessTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "RoughnessTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~RoughnessTexture.html"
---

# RoughnessTexture Property (IDSPBRMaterial)

Sets or sets the surface roughness texture map for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property RoughnessTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.RoughnessTexture = value

value = instance.RoughnessTexture
```

### C#

```csharp
System.string RoughnessTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ RoughnessTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the roughness texture map

## VBA Syntax

See [DSPBRMaterial::RoughnessTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~RoughnessTexture.html).

## Remarks

Search for "Roughness texture maps in materials" on the web to obtain more information about this property.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
