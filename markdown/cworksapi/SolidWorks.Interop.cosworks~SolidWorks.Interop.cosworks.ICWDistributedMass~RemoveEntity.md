---
title: "RemoveEntity Method (ICWDistributedMass)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDistributedMass"
member: "RemoveEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass~RemoveEntity.html"
---

# RemoveEntity Method (ICWDistributedMass)

Removes a face or shell edge from the collection of entities on which to distribute the mass.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDistributedMass
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

See [CWDistributedMass::RemoveEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDistributedMass~RemoveEntity.html).

## See Also

[ICWDistributedMass Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass.html)
[ICWDistributedMass Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass_members.html)
[ICWDistributedMass::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass~InsertEntity.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
