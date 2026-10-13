---
title: "NormalTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "NormalTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~NormalTexture.html"
---

# NormalTexture Property (IDSPBRMaterial)

Gets or sets the normal texture map for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property NormalTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.NormalTexture = value

value = instance.NormalTexture
```

### C#

```csharp
System.string NormalTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ NormalTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the normal texture map

## VBA Syntax

See [DSPBRMaterial::NormalTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~NormalTexture.html).

## Remarks

Search for "Normal texture map" on the web to obtain more information about this property.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
