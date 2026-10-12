---
title: "MappingType Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "MappingType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MappingType.html"
---

# MappingType Property (IRenderMaterial)

Gets or sets the mapping type for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property MappingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.MappingType = value

value = instance.MappingType
```

### C#

```csharp
System.int MappingType {get; set;}
```

### C++/CLI

```cpp
property System.int MappingType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- 0 = Surface

1 = Projection

2 = Spherical

3 = Cylindrical

4 = Automatic

## VBA Syntax

See [RenderMaterial::MappingType](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~MappingType.html).

## Examples

See the "Add Decal" examples in [IRenderMaterial::FileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FileName.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
