---
title: "ElementSize Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "ElementSize"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~ElementSize.html"
---

# ElementSize Property (ICWMeshControl)

Gets or sets the element size of the mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property ElementSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Double

instance.ElementSize = value

value = instance.ElementSize
```

### C#

```csharp
System.double ElementSize {get; set;}
```

### C++/CLI

```cpp
property System.double ElementSize {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Element size (see **Remarks**)

## VBA Syntax

See [CWMeshControl::ElementSize](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~ElementSize.html).

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## Remarks

This property gets or sets the global element size for standard meshes and the maximum element size for curvature-based meshes. To get or set the minimum element size for curvature-based meshes, call [ICWMeshControl::MinimumElementSizeForBlendedCurveMesher](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinimumElementSizeForBlendedCurveMesher.html).

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::UseSameElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~UseSameElementSize.html)
[ICWMeshControl::NumofElementsforBeams Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~NumofElementsforBeams.html)
[ICWMeshControl::MinNumOfElementsPerCircleForBlendedCurveMesher Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~MinNumOfElementsPerCircleForBlendedCurveMesher.html)
[ICWMeshControl::Ratio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~Ratio.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
