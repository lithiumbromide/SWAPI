---
title: "AutomaticLooping Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "AutomaticLooping"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticLooping.html"
---

# AutomaticLooping Property (ICWMesh)

Obsolete. Superseded by [ICWMesh::AutomaticLooping2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticLooping2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property AutomaticLooping As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.AutomaticLooping = value

value = instance.AutomaticLooping
```

### C#

```csharp
System.int AutomaticLooping {get; set;}
```

### C++/CLI

```cpp
property System.int AutomaticLooping {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 if automatic looping is on, 0 if not

## VBA Syntax

See [CWMesh::AutomaticLooping](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~AutomaticLooping.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::NumberOfLoops Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NumberOfLoops.html)
[ICWMesh::NumberOfLoops Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NumberOfLoops.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
