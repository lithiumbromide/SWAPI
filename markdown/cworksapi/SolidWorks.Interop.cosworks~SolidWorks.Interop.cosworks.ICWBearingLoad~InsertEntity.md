---
title: "InsertEntity Method (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "InsertEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~InsertEntity.html"
---

# InsertEntity Method (ICWBearingLoad)

Inserts a source entity for the bearing load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
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

- `DispEntity`: Source entity (cylindrical face)

## VBA Syntax

See [CWBearingLoad::InsertEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~InsertEntity.html).

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)
[ICWBearingLoad::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~RemoveEntity.html)
[ICWBearingLoad::GetEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~GetEntityCount.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
