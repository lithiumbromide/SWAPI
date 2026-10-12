---
title: "EmissionColorTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "EmissionColorTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~EmissionColorTexture.html"
---

# EmissionColorTexture Property (IDSPBRMaterial)

Gets or sets the emission color texture map for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property EmissionColorTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.EmissionColorTexture = value

value = instance.EmissionColorTexture
```

### C#

```csharp
System.string EmissionColorTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ EmissionColorTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the emission color texture map

## VBA Syntax

See [DSPBRMaterial::EmissionColorTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~EmissionColorTexture.html).

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
