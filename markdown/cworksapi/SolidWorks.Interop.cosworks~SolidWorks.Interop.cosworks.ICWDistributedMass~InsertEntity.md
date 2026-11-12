---
title: "InsertEntity Method (ICWDistributedMass)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDistributedMass"
member: "InsertEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass~InsertEntity.html"
---

# InsertEntity Method (ICWDistributedMass)

Adds a face or shell edge to the collection of entities on which to distribute the mass.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertEntity( _
   ByVal DispEntity As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDistributedMass
Dim DispEntity As System.Object
Dim value As System.Integer

value = instance.InsertEntity(DispEntity)
```

### C#

```csharp
System.int InsertEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
System.int InsertEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Face or edge

### Return Value

Index of entity added

## VBA Syntax

See [CWDistributedMass::InsertEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDistributedMass~InsertEntity.html).

## See Also

[ICWDistributedMass Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass.html)
[ICWDistributedMass Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass_members.html)
[ICWDistributedMass::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
