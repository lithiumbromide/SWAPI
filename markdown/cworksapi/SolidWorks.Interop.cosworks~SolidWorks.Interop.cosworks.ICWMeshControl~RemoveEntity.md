---
title: "RemoveEntity Method (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "RemoveEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~RemoveEntity.html"
---

# RemoveEntity Method (ICWMeshControl)

Removes the specified entity from the mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim NIndex As System.Integer

instance.RemoveEntity(NIndex)
```

### C#

```csharp
void RemoveEntity(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveEntity(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of entity to remove

## VBA Syntax

See [CWMeshControl::RemoveEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~RemoveEntity.html).

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::GetEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~GetEntityAt.html)
[ICWMeshControl::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~InsertEntity.html)
[ICWMeshControl::EntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~EntityCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
