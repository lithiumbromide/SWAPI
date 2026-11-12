---
title: "SmoothSurface Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "SmoothSurface"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~SmoothSurface.html"
---

# SmoothSurface Property (ICWMesh)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Property SmoothSurface As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.SmoothSurface = value

value = instance.SmoothSurface
```

### C#

```csharp
System.int SmoothSurface {get; set;}
```

### C++/CLI

```cpp
property System.int SmoothSurface {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 if on, 0 if off

## VBA Syntax

See [CWMesh::SmoothSurface](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~SmoothSurface.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
