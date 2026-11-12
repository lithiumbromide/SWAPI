---
title: "InsertTightFitEntity Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "InsertTightFitEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertTightFitEntity.html"
---

# InsertTightFitEntity Method (ICWBoltConnector)

Inserts the entity (shank contact face) for a tight fit.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertTightFitEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim DispEntity As System.Object

instance.InsertTightFitEntity(DispEntity)
```

### C#

```csharp
void InsertTightFitEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertTightFitEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Entity (shank contact face)

## VBA Syntax

See [CWBoltConnector::InsertTightFitEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~InsertTightFitEntity.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::RemoveTightFitEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveTightFitEntity.html)
[ICWBoltConnector::IncludeTightFit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeTightFit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
