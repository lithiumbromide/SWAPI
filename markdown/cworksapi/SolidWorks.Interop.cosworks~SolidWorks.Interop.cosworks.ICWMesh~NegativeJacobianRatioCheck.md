---
title: "NegativeJacobianRatioCheck Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "NegativeJacobianRatioCheck"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NegativeJacobianRatioCheck.html"
---

# NegativeJacobianRatioCheck Property (ICWMesh)

Obsolete. Superseded by [ICWMesh::NegativeJacobianRatioCheck2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NegativeJacobianRatioCheck2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property NegativeJacobianRatioCheck As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.NegativeJacobianRatioCheck = value

value = instance.NegativeJacobianRatioCheck
```

### C#

```csharp
System.int NegativeJacobianRatioCheck {get; set;}
```

### C++/CLI

```cpp
property System.int NegativeJacobianRatioCheck {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to check for a negative Jacobian ratio, 0 to not

## VBA Syntax

See [CWMesh::NegativeJacobianRatioCheck](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~NegativeJacobianRatioCheck.html).

## Remarks

For more information, read the **Jacobian Points** section of the **Simulation > Meshing >** **Mesh Quality Checks** topic in the SOLIDWORKS help.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::JacobianPoints Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~JacobianPoints.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
