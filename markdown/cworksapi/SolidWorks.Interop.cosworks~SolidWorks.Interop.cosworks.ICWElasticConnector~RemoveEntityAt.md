---
title: "RemoveEntityAt Method (ICWElasticConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWElasticConnector"
member: "RemoveEntityAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~RemoveEntityAt.html"
---

# RemoveEntityAt Method (ICWElasticConnector)

Removes an entity at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntityAt( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWElasticConnector
Dim NIndex As System.Integer

instance.RemoveEntityAt(NIndex)
```

### C#

```csharp
void RemoveEntityAt(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveEntityAt(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index at which to remove the entity

## VBA Syntax

See [CWElasticConnector::RemoveEntityAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWElasticConnector~RemoveEntityAt.html).

## Remarks

Before calling this method, call [ICWElasticConnector::GetEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWElasticConnector~GetEntityCount.html) to determine the value of NIndex.

## See Also

[ICWElasticConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector.html)
[ICWElasticConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector_members.html)
[ICWElasticConnector::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWElasticConnector~InsertEntity.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
