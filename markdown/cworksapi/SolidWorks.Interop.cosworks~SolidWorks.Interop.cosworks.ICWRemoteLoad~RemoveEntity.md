---
title: "RemoveEntity Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "RemoveEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~RemoveEntity.html"
---

# RemoveEntity Method (ICWRemoteLoad)

Removes a face, edge, or vertex from the collection of entities to which this remote load is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
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

- `NIndex`: Index of entity to remove

## VBA Syntax

See [CWRemoteLoad::RemoveEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~RemoveEntity.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~InsertEntity.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
