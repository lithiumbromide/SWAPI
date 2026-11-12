---
title: "ElementCount Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "ElementCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementCount.html"
---

# ElementCount Property (ICWMesh)

Gets the number of elements in the mesh.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ElementCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

value = instance.ElementCount
```

### C#

```csharp
System.int ElementCount {get;}
```

### C++/CLI

```cpp
property System.int ElementCount {
   System.int get();
}
```

### Property Value

Number of elements in the mesh

## VBA Syntax

See [CWMesh::ElementCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~ElementCount.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetDefaultElementSizeAndTolerance Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultElementSizeAndTolerance.html)
[ICWMesh::GetElementDataFromEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementDataFromEntity.html)
[ICWMesh::GetElementLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementLocation.html)
[ICWMesh::GetElements Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElements.html)
[ICWMesh::ElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementSize.html)
[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)
[ICWMesh::MaxAspectRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxAspectRatio.html)
[ICWResults::GetStressTensorValuesForAllNodesOfElement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressTensorValuesForAllNodesOfElement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
