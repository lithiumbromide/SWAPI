---
title: "AlbedoTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "AlbedoTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~AlbedoTexture.html"
---

# AlbedoTexture Property (IDSPBRMaterial)

Gets or sets the Albedo texture map for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlbedoTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.AlbedoTexture = value

value = instance.AlbedoTexture
```

### C#

```csharp
System.string AlbedoTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ AlbedoTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the Albedo texture map for this material.

## VBA Syntax

See [DSPBRMaterial::AlbedoTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~AlbedoTexture.html).

## Remarks

Search for "Albedo texture" in the web to obtain more information about this property.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
