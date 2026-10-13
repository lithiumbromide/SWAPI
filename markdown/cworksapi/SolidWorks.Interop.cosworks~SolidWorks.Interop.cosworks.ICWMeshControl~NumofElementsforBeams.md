---
title: "NumofElementsforBeams Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "NumofElementsforBeams"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~NumofElementsforBeams.html"
---

# NumofElementsforBeams Property (ICWMeshControl)

Gets or sets the total number of mesh elements for selected beams.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumofElementsforBeams As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Integer

instance.NumofElementsforBeams = value

value = instance.NumofElementsforBeams
```

### C#

```csharp
System.int NumofElementsforBeams {get; set;}
```

### C++/CLI

```cpp
property System.int NumofElementsforBeams {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of mesh elements for selected beams

## VBA Syntax

See [CWMeshControl::NumofElementsforBeams](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~NumofElementsforBeams.html).

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## Remarks

This property is valid only for beams.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::ElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~ElementSize.html)
[ICWMeshControl::UseSameElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~UseSameElementSize.html)
[ICWMeshControl::BeamSelected Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~BeamSelected.html)

## Availability

SOLIDWORKS Simulation API 2011 SP0
