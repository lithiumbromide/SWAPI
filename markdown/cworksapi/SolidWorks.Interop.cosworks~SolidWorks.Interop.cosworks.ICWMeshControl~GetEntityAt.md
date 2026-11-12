---
title: "GetEntityAt Method (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "GetEntityAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~GetEntityAt.html"
---

# GetEntityAt Method (ICWMeshControl)

Obsolete. Superseded by [ICWMeshControl::GetEntityAt2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~GetEntityAt2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityAt( _
   ByVal NIndex As System.Integer, _
   ByRef NSelectionType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim NIndex As System.Integer
Dim NSelectionType As System.Integer
Dim value As System.Object

value = instance.GetEntityAt(NIndex, NSelectionType)
```

### C#

```csharp
System.object GetEntityAt(
   System.int NIndex,
   out System.int NSelectionType
)
```

### C++/CLI

```cpp
System.Object^ GetEntityAt(
   System.int NIndex,
   [Out] System.int NSelectionType
)
```

### Parameters

- `NIndex`: 0-based index of entity
- `NSelectionType`: Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Entity

## VBA Syntax

See [CWMeshControl::GetEntityAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~GetEntityAt.html).

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~InsertEntity.html)
[ICWMeshControl::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~RemoveEntity.html)
[ICWMeshControl::EntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~EntityCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
