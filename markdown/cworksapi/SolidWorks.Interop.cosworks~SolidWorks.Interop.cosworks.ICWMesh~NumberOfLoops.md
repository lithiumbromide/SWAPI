---
title: "NumberOfLoops Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "NumberOfLoops"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NumberOfLoops.html"
---

# NumberOfLoops Property (ICWMesh)

Gets or sets the number of loops for automatic mesh looping.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfLoops As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.NumberOfLoops = value

value = instance.NumberOfLoops
```

### C#

```csharp
System.int NumberOfLoops {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfLoops {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of loops

## VBA Syntax

See [CWMesh::NumberOfLoops](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~NumberOfLoops.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::AutomaticLooping Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticLooping.html)
[ICWMesh::GetDefaultElementSizeAndTolerance Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultElementSizeAndTolerance.html)

## Availability

SOLIDWORKS Simulation API 2008 SP.10
