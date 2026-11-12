---
title: "MinimumElementSizeForBlendedCurveMesher Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "MinimumElementSizeForBlendedCurveMesher"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinimumElementSizeForBlendedCurveMesher.html"
---

# MinimumElementSizeForBlendedCurveMesher Property (ICWMeshControl)

Gets and sets the minimum element size for a curvature-based mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinimumElementSizeForBlendedCurveMesher As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Double

instance.MinimumElementSizeForBlendedCurveMesher = value

value = instance.MinimumElementSizeForBlendedCurveMesher
```

### C#

```csharp
System.double MinimumElementSizeForBlendedCurveMesher {get; set;}
```

### C++/CLI

```cpp
property System.double MinimumElementSizeForBlendedCurveMesher {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Minimum element size

## VBA Syntax

See [CWMeshControl::MinimumElementSizeForBlendedCurveMesher](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~MinimumElementSizeForBlendedCurveMesher.html).

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## Remarks

This property is valid only if:

- [ICWMeshControl::BeamSelected](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~BeamSelected.html) = 0
- [ICWMesh::MesherType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MesherType.html) = [swsMesherType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMesherType_e.html).swsMesherTypeAlternateCB

To get and set the maximum element size for a curvature-based mesh, call [ICWMeshControl::ElementSize](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~ElementSize.html).

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::MinNumOfElementsPerCircleForBlendedCurveMesher Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinNumOfElementsPerCircleForBlendedCurveMesher.html)
[ICWMeshControl::Ratio Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~Ratio.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
