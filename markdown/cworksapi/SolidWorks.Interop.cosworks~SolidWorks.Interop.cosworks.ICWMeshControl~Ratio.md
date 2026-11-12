---
title: "Ratio Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "Ratio"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~Ratio.html"
---

# Ratio Property (ICWMeshControl)

Gets or sets the ratio of the average element size for element layer (i) to that of layer (i-1) for this mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Property Ratio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Double

instance.Ratio = value

value = instance.Ratio
```

### C#

```csharp
System.double Ratio {get; set;}
```

### C++/CLI

```cpp
property System.double Ratio {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Ratio of the average element size for element layer (i) to that of layer (i-1)

## VBA Syntax

See [CWMeshControl::Ratio](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~Ratio.html).

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## Remarks

This property is valid only if [ICWMesh::MesherType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MesherType.html) =

- [swsMesherType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMesherType_e.html).swsMesherTypeAlternate

- or -

- swsMesherType_e.swsMesherTypeAlternateCB

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::MinNumOfElementsPerCircleForBlendedCurveMesher Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinNumOfElementsPerCircleForBlendedCurveMesher.html)
[ICWMeshControl::MinimumElementSizeForBlendedCurveMesher Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinimumElementSizeForBlendedCurveMesher.html)
[ICWMeshControl::ElementSize Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~ElementSize.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
