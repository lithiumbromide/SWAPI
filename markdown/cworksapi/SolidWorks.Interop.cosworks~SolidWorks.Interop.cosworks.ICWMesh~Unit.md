---
title: "Unit Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "Unit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~Unit.html"
---

# Unit Property (ICWMesh)

Gets the units for the mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.Unit = value

value = instance.Unit
```

### C#

```csharp
System.int Unit {get; set;}
```

### C++/CLI

```cpp
property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Mesh linear units as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWMesh::Unit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~Unit.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS Simulation API 2011 SP0
