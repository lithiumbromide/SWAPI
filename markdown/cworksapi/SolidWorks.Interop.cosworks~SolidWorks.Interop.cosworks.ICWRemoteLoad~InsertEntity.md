---
title: "InsertEntity Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "InsertEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~InsertEntity.html"
---

# InsertEntity Method (ICWRemoteLoad)

Adds a face, edge, or vertex to the collection of entities to which this remote load is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim DispEntity As System.Object

instance.InsertEntity(DispEntity)
```

### C#

```csharp
void InsertEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Entity (see **Remarks**)

### Return Value

Index of entity added

## VBA Syntax

See [CWRemoteLoad::InsertEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~InsertEntity.html).

## Remarks

| If ICWRemoteLoad::LoadType is ... | DispEntity is ... |
| --- | --- |
| swsRemoteLoadType_e.swsRemoteLoadType_DirectLoad | Face |
| swsRemoteLoadType_e.swsRemoteLoadType_RigidLoadOrMass | Face or edge |
| swsRemoteLoadType_e.swsRemoteLoadType_RigidDisplacement | Face or edge |
| swsRemoteLoadType_e.swsRemoteLoadType_DirectDisplacement | Face, edge, or vertex |

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
