---
title: "RemoveEntityAtFirstLocation Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "RemoveEntityAtFirstLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveEntityAtFirstLocation.html"
---

# RemoveEntityAtFirstLocation Method (ICWBoltConnector)

Removes the source entity at the specified index at the first location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntityAtFirstLocation( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim NIndex As System.Integer

instance.RemoveEntityAtFirstLocation(NIndex)
```

### C#

```csharp
void RemoveEntityAtFirstLocation(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveEntityAtFirstLocation(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index at which to remove the source entity at the first location

### Return Value

Call [ICWBoltConnector::GetSourceEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBoltConnector~GetSourceEntityCount.html) before calling this method to get a valid index.

## VBA Syntax

See [CWBoltConnector::RemoveEntityAtFirstLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~RemoveEntityAtFirstLocation.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::RemoveEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveEntityAtSecondLocation.html)
[ICWBoltConnector::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertEntityAtFirstLocation.html)
[ICWBoltConnector::InsertEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertEntityAtSecondLocation.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
