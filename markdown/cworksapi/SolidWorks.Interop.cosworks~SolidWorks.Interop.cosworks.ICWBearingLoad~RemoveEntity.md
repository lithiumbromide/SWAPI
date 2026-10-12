---
title: "RemoveEntity Method (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "RemoveEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~RemoveEntity.html"
---

# RemoveEntity Method (ICWBearingLoad)

Removes a source entity at the specified index from the bearing load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
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

- `NIndex`: 0-based index of the source entity to remove

## VBA Syntax

See [CWBearingLoad::RemoveEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~RemoveEntity.html).

## Remarks

Call [ICWBearingLoad::GetEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBearingLoad~GetEntityCount.html) before calling this method to get a valid index.

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)
[ICWBearingLoad::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~InsertEntity.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
