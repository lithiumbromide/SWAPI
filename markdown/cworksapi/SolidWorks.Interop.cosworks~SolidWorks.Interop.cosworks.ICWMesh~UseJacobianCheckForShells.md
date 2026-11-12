---
title: "UseJacobianCheckForShells Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "UseJacobianCheckForShells"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForShells.html"
---

# UseJacobianCheckForShells Property (ICWMesh)

Obsolete. Superseded by [ICWMesh::UseJacobianCheckForShells2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForShells2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseJacobianCheckForShells As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.UseJacobianCheckForShells = value

value = instance.UseJacobianCheckForShells
```

### C#

```csharp
System.int UseJacobianCheckForShells {get; set;}
```

### C++/CLI

```cpp
property System.int UseJacobianCheckForShells {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to perform the Jacobian check, 0 to not

## VBA Syntax

See [CWMesh::UseJacobianCheckForShells](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~UseJacobianCheckForShells.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::UseJacobianCheckForSolids Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForSolids.html)
[ICWMesh::GetWorstJacobianRatio Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetWorstJacobianRatio.html)
[ICWMesh::JacobianPoints Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~JacobianPoints.html)
[ICWMesh::NegativeJacobianRatioCheck Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NegativeJacobianRatioCheck.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
