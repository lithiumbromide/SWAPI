---
title: "Material Property (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "Material"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~Material.html"
---

# Material Property (IImport3DInterconnectData)

Gets or sets whether to import material properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property Material As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim value As System.Boolean

instance.Material = value

value = instance.Material
```

### C#

```csharp
System.bool Material {get; set;}
```

### C++/CLI

```cpp
property System.bool Material {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import material name and density attributes, false to not

## VBA Syntax

See [Import3DInterconnectData::Material](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~Material.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
