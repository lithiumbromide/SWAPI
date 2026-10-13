---
title: "ElementSizeFactorForEachLoop Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "ElementSizeFactorForEachLoop"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementSizeFactorForEachLoop.html"
---

# ElementSizeFactorForEachLoop Property (ICWMesh)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Property ElementSizeFactorForEachLoop As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Double

instance.ElementSizeFactorForEachLoop = value

value = instance.ElementSizeFactorForEachLoop
```

### C#

```csharp
System.double ElementSizeFactorForEachLoop {get; set;}
```

### C++/CLI

```cpp
property System.double ElementSizeFactorForEachLoop {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Element size factor for looping

## VBA Syntax

See [CWMesh::ElementSizeFactorForEachLoop](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~ElementSizeFactorForEachLoop.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetDefaultElementSizeAndTolerance Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultElementSizeAndTolerance.html)
[ICWMesh::GetElementDataFromEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementDataFromEntity.html)
[ICWMesh::GetElementLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementLocation.html)
[ICWMesh::GetElements Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElements.html)
[ICWMesh::ElementCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementCount.html)
[ICWMesh::ElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementSize.html)
[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)
[ICWMesh::MaxAspectRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxAspectRatio.html)

## Availability

Simulation Simulation API 2008 SP1.0
