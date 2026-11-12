---
title: "RemoveEntityAtFirstLocation Method (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "RemoveEntityAtFirstLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RemoveEntityAtFirstLocation.html"
---

# RemoveEntityAtFirstLocation Method (ICWSpringConnector)

Remove the entity at the specified index from the first location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntityAtFirstLocation( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
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

- `NIndex`: 0-based index at which to remove the entity

## VBA Syntax

See [CWSpringConnector::RemoveEntityAtFirstLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~RemoveEntityAtFirstLocation.html).

## Remarks

Before calling this method, call [ICWSpringConnector::GetSourceEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSpringConnector~GetSourceEntityCount.html) to determine the value of NIndex.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringConnector::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~InsertEntityAtFirstLocation.html)
[ICWSpringConnector::GetTargetEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~GetTargetEntityCount.html)
[ICWSpringConnector::InsertEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~InsertEntityAtSecondLocation.html)
[ICWSpringConnector::RemoveEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RemoveEntityAtSecondLocation.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
