---
title: "MinNumOfElementsPerCircleForBlendedCurveMesher Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "MinNumOfElementsPerCircleForBlendedCurveMesher"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinNumOfElementsPerCircleForBlendedCurveMesher.html"
---

# MinNumOfElementsPerCircleForBlendedCurveMesher Property (ICWMeshControl)

Gets and sets the minimum number of elements in a circle to determine the maximum angle in a curvature-based mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinNumOfElementsPerCircleForBlendedCurveMesher As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Integer

instance.MinNumOfElementsPerCircleForBlendedCurveMesher = value

value = instance.MinNumOfElementsPerCircleForBlendedCurveMesher
```

### C#

```csharp
System.int MinNumOfElementsPerCircleForBlendedCurveMesher {get; set;}
```

### C++/CLI

```cpp
property System.int MinNumOfElementsPerCircleForBlendedCurveMesher {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Minimum number of elements in a circle

## VBA Syntax

See [CWMeshControl::MinNumOfElementsPerCircleForBlendedCurveMesher](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~MinNumOfElementsPerCircleForBlendedCurveMesher.html).

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## Remarks

This property is valid only if:

- [ICWMeshControl::BeamSelected](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~BeamSelected.html) = 0
- [ICWMesh::MesherType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MesherType.html)=

  - [swsMesherType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMesherType_e.html).swsMesherTypeAlternateCB

- or -

- swsMesherType_e.swsMesherTypeAlternate

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::ElementSize Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~ElementSize.html)
[ICWMeshControl::Ratio Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~Ratio.html)
[ICWMeshControl::MinimumElementSizeForBlendedCurveMesher Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinimumElementSizeForBlendedCurveMesher.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
