---
title: "AutomaticTransition Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "AutomaticTransition"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticTransition.html"
---

# AutomaticTransition Property (ICWMesh)

Obsolete. Superseded by [ICWMesh::AutomaticTransition2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticTransition2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property AutomaticTransition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.AutomaticTransition = value

value = instance.AutomaticTransition
```

### C#

```csharp
System.int AutomaticTransition {get; set;}
```

### C++/CLI

```cpp
property System.int AutomaticTransition {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 if automatic transition is on, 0 if not

## VBA Syntax

See [CWMesh::AutomaticTransition](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~AutomaticTransition.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::ApplyMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ApplyMeshControl.html)
[ICWMesh::DeleteMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~DeleteMeshControl.html)
[ICWMesh::GetMeshControlAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetMeshControlAt.html)
[ICWMesh::MeshControlCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshControlCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
