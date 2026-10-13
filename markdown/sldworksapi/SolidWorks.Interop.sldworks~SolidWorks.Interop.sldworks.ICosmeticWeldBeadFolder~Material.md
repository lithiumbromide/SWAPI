---
title: "Material Property (ICosmeticWeldBeadFolder)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFolder"
member: "Material"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder~Material.html"
---

# Material Property (ICosmeticWeldBeadFolder)

Gets or sets the material of the weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Property Material As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFolder
Dim value As System.String

instance.Material = value

value = instance.Material
```

### C#

```csharp
System.string Material {get; set;}
```

### C++/CLI

```cpp
property System.String^ Material {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weld material

## VBA Syntax

See [CosmeticWeldBeadFolder::Material](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFolder~Material.html).

## Examples

See [ICosmeticWeldBeadFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFolder.html) examples.

## See Also

[ICosmeticWeldBeadFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder.html)
[ICosmeticWeldBeadFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
