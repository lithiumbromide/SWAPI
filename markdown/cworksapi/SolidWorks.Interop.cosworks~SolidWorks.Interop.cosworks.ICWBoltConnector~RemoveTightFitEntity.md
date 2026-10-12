---
title: "RemoveTightFitEntity Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "RemoveTightFitEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveTightFitEntity.html"
---

# RemoveTightFitEntity Method (ICWBoltConnector)

Removes the entity at the specified index from a tight fit.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveTightFitEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim NIndex As System.Integer

instance.RemoveTightFitEntity(NIndex)
```

### C#

```csharp
void RemoveTightFitEntity(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveTightFitEntity(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of entity to removed from a tight fit

## VBA Syntax

See [CWBoltConnector::RemoveTightFitEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~RemoveTightFitEntity.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::InsertTightFitEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertTightFitEntity.html)
[ICWBoltConnector::IncludeTightFit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeTightFit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
