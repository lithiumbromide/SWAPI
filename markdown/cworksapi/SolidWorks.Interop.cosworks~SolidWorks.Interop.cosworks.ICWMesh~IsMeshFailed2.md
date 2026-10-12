---
title: "IsMeshFailed2 Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "IsMeshFailed2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsMeshFailed2.html"
---

# IsMeshFailed2 Property (ICWMesh)

Checks the status of the mesh.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsMeshFailed2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Boolean

value = instance.IsMeshFailed2
```

### C#

```csharp
System.bool IsMeshFailed2 {get;}
```

### C++/CLI

```cpp
property System.bool IsMeshFailed2 {
   System.bool get();
}
```

### Property Value

-1 or true if mesh failed, 0 or false if not

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
