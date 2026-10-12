---
title: "RemoveEntityAtSecondLocation Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "RemoveEntityAtSecondLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveEntityAtSecondLocation.html"
---

# RemoveEntityAtSecondLocation Method (ICWBoltConnector)

Removes the target entity at the specified index at the second location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntityAtSecondLocation( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim NIndex As System.Integer

instance.RemoveEntityAtSecondLocation(NIndex)
```

### C#

```csharp
void RemoveEntityAtSecondLocation(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveEntityAtSecondLocation(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of the target entity to remove at the second location

## VBA Syntax

See [CWBoltConnector::RemoveEntityAtSecondLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~RemoveEntityAtSecondLocation.html).

## Remarks

Call [ICWBoltConnector::GetTargetEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBoltConnector~GetTargetEntityCount.html) before calling this method to get a valid index.

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
