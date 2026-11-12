---
title: "InsertEntity Method (ICWElasticConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWElasticConnector"
member: "InsertEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~InsertEntity.html"
---

# InsertEntity Method (ICWElasticConnector)

Inserts an entity into this elastic support fixture.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWElasticConnector
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

- `DispEntity`: Entity

## VBA Syntax

See [CWElasticConnector::InsertEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWElasticConnector~InsertEntity.html).

## See Also

[ICWElasticConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html)
[ICWElasticConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector_members.html)
[ICWElasticConnector::GetEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~GetEntityCount.html)
[ICWElasticConnector::RemoveEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~RemoveEntityAt.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
