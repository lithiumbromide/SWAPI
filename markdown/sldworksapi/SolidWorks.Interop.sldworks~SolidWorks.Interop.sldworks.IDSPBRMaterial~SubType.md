---
title: "SubType Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "SubType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~SubType.html"
---

# SubType Property (IDSPBRMaterial)

Gets or sets the subtype of this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property SubType As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.String

instance.SubType = value

value = instance.SubType
```

### C#

```csharp
System.string SubType {get; set;}
```

### C++/CLI

```cpp
property System.String^ SubType {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of this material's subtype

## VBA Syntax

See [DSPBRMaterial::SubType](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~SubType.html).

## Remarks

Use the following subtypes to expose subsets of parameters:

"Car Paint"

"Metal"

"Emissive"

"Textile"

"Leather"

"Wood"

"Glass"

"Plastic"

For more information about this property:

- Open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser, click CTRL-F and type "Material Subtypes" in the pop up. Click **Next result** repeatedly.

- Search for "Accessing Material Types" on the web.

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
