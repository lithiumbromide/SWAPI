---
title: "GetNodeLocation Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetNodeLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeLocation.html"
---

# GetNodeLocation Method (ICWMesh)

Gets the coordinates of the specified node.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNodeLocation( _
   ByVal NNodeNo As System.Integer, _
   ByRef XVal As System.Double, _
   ByRef YVal As System.Double, _
   ByRef ZVal As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim NNodeNo As System.Integer
Dim XVal As System.Double
Dim YVal As System.Double
Dim ZVal As System.Double
Dim value As System.Integer

value = instance.GetNodeLocation(NNodeNo, XVal, YVal, ZVal)
```

### C#

```csharp
System.int GetNodeLocation(
   System.int NNodeNo,
   out System.double XVal,
   out System.double YVal,
   out System.double ZVal
)
```

### C++/CLI

```cpp
System.int GetNodeLocation(
   System.int NNodeNo,
   [Out] System.double XVal,
   [Out] System.double YVal,
   [Out] System.double ZVal
)
```

### Parameters

- `NNodeNo`: Node number
- `XVal`: X coordinate
- `YVal`: Y coordinate
- `ZVal`: Z coordinate

### Return Value

Error as defined in [swsMeshControlError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshControlError_e.html)

## VBA Syntax

See [CWMesh::GetNodeLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetNodeLocation.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetNodeDataFromEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeDataFromEntity.html)
[ICWMesh::GetNodes Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodes.html)
[ICWMesh::NodeCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NodeCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
