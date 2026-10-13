---
title: "UseJacobianCheckForSolids Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "UseJacobianCheckForSolids"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForSolids.html"
---

# UseJacobianCheckForSolids Property (ICWMesh)

Gets or sets whether to perform a Jacobian check for solids.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseJacobianCheckForSolids As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.UseJacobianCheckForSolids = value

value = instance.UseJacobianCheckForSolids
```

### C#

```csharp
System.int UseJacobianCheckForSolids {get; set;}
```

### C++/CLI

```cpp
property System.int UseJacobianCheckForSolids {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to check the Jacobian for solids, 0 to not

## VBA Syntax

See [CWMesh::UseJacobianCheckForSolids](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~UseJacobianCheckForSolids.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetWorstJacobianRatio Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetWorstJacobianRatio.html)
[ICWMesh::NegativeJacobianRatioCheck Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NegativeJacobianRatioCheck.html)
[ICWMesh::JacobianPoints Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~JacobianPoints.html)
[ICWMesh::UseJacobianCheckForShells Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForShells.html)
[ICWMesh::UseJacobianCheckForSolids Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForSolids.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
