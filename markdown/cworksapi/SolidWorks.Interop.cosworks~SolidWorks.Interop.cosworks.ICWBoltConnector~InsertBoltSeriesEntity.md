---
title: "InsertBoltSeriesEntity Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "InsertBoltSeriesEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertBoltSeriesEntity.html"
---

# InsertBoltSeriesEntity Method (ICWBoltConnector)

Inserts an entity (cylindrical face from the middle components) in the bolt series.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertBoltSeriesEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim DispEntity As System.Object

instance.InsertBoltSeriesEntity(DispEntity)
```

### C#

```csharp
void InsertBoltSeriesEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertBoltSeriesEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Entity (cylindrical face from the middle components)

## VBA Syntax

See [CWBoltConnector::InsertBoltSeriesEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~InsertBoltSeriesEntity.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::RemoveBoltSeriesEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveBoltSeriesEntity.html)
[ICWBoltConnector::IncludeBoltSeries Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeBoltSeries.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
