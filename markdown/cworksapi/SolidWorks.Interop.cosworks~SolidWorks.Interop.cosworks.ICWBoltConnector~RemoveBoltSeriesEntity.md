---
title: "RemoveBoltSeriesEntity Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "RemoveBoltSeriesEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveBoltSeriesEntity.html"
---

# RemoveBoltSeriesEntity Method (ICWBoltConnector)

Removes the entity at the specified index from a bolt series.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveBoltSeriesEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim NIndex As System.Integer

instance.RemoveBoltSeriesEntity(NIndex)
```

### C#

```csharp
void RemoveBoltSeriesEntity(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveBoltSeriesEntity(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index at which to remove the entity

## VBA Syntax

See [CWBoltConnector::RemoveBoltSeriesEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~RemoveBoltSeriesEntity.html).

## Remarks

Call [ICWBoltConnector::GetBoltSeriesEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBoltConnector~GetBoltSeriesEntityCount.html) to determine the value of NIndex.

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::RemoveBoltSeriesEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveBoltSeriesEntity.html)
[ICWBoltConnector::IncludeBoltSeries Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeBoltSeries.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
