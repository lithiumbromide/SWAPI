---
title: "Tolerance Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "Tolerance"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~Tolerance.html"
---

# Tolerance Property (ICWMesh)

Gets the tolerance value for mesh loops.

## Syntax

### Visual Basic (Declaration)

```vb
Property Tolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Double

instance.Tolerance = value

value = instance.Tolerance
```

### C#

```csharp
System.double Tolerance {get; set;}
```

### C++/CLI

```cpp
property System.double Tolerance {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Tolerance value for mesh loops

## VBA Syntax

See [CWMesh::Tolerance](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~Tolerance.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
