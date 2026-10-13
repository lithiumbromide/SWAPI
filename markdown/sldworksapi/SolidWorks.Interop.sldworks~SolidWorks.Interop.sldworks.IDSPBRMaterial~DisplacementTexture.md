---
title: "DisplacementTexture Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "DisplacementTexture"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~DisplacementTexture.html"
---

# DisplacementTexture Property (IDSPBRMaterial)

Gets or sets the displacement texture map for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplacementTexture As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.DisplacementTexture = value

value = instance.DisplacementTexture
```

### C#

```csharp
System.string DisplacementTexture {get; set;}
```

### C++/CLI

```cpp
property System.String^ DisplacementTexture {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Displacement texture map

## VBA Syntax

See [DSPBRMaterial::DisplacementTexture](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~DisplacementTexture.html).

## Remarks

For more information about this property, search for "displacement texture map" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
