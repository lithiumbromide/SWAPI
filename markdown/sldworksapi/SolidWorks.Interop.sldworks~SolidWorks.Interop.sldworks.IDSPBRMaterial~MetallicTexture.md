---
title: "MetallicTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "MetallicTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~MetallicTexture.html"
---

# MetallicTexture Property (IDSPBRMaterial)

Gets or sets the metallic texture of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property MetallicTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.MetallicTexture = value

value = instance.MetallicTexture
```

### C#

```csharp
System.string MetallicTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ MetallicTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the metallic texture map

## VBA Syntax

See [DSPBRMaterial::MetallicTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~MetallicTexture.html).

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
