---
title: "BeamSelected Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "BeamSelected"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~BeamSelected.html"
---

# BeamSelected Property (ICWMeshControl)

Obsolete. Superseded by [ICWMeshControl::BeamSelected2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~BeamSelected2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property BeamSelected As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Integer

instance.BeamSelected = value

value = instance.BeamSelected
```

### C#

```csharp
System.int BeamSelected {get; set;}
```

### C++/CLI

```cpp
property System.int BeamSelected {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to select beams, 0 to not

## VBA Syntax

See [CWMeshControl::BeamSelected](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~BeamSelected.html).

## Remarks

This property is only valid for models with beams.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::NumofElementsforBeams Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~NumofElementsforBeams.html)
[ICWMeshControl::MinimumElementSizeForBlendedCurveMesher Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinimumElementSizeForBlendedCurveMesher.html)
[ICWMeshControl::MinNumOfElementsPerCircleForBlendedCurveMesher Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinNumOfElementsPerCircleForBlendedCurveMesher.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
