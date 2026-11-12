---
title: "TimeToCompleteMesh Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "TimeToCompleteMesh"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~TimeToCompleteMesh.html"
---

# TimeToCompleteMesh Property (ICWMesh)

Gets the estimated time to complete the mesh.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TimeToCompleteMesh As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

value = instance.TimeToCompleteMesh
```

### C#

```csharp
System.int TimeToCompleteMesh {get;}
```

### C++/CLI

```cpp
property System.int TimeToCompleteMesh {
   System.int get();
}
```

### Property Value

Estimated time to complete the mesh formatted as hh:mm:ss; e.g., return value 12 equals 12 seconds

## VBA Syntax

See [CWMesh::TimeToCompleteMesh](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~TimeToCompleteMesh.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
