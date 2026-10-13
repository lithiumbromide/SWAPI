---
title: "EntityCount Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "EntityCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~EntityCount.html"
---

# EntityCount Property (ICWMeshControl)

Gets the number of entities in the mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property EntityCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Integer

value = instance.EntityCount
```

### C#

```csharp
System.int EntityCount {get;}
```

### C++/CLI

```cpp
property System.int EntityCount {
   System.int get();
}
```

### Property Value

Number of entities in the mesh control

## VBA Syntax

See [CWMeshControl::EntityCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~EntityCount.html).

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::GetEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~GetEntityAt.html)
[ICWMeshControl::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~InsertEntity.html)
[ICWMeshControl::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
