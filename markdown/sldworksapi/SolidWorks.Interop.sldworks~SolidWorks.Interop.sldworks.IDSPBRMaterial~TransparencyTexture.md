---
title: "TransparencyTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "TransparencyTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~TransparencyTexture.html"
---

# TransparencyTexture Property (IDSPBRMaterial)

Gets or sets the transparency texture of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransparencyTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.TransparencyTexture = value

value = instance.TransparencyTexture
```

### C#

```csharp
System.string TransparencyTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ TransparencyTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the transparency texture map

## VBA Syntax

See [DSPBRMaterial::TransparencyTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~TransparencyTexture.html).

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
