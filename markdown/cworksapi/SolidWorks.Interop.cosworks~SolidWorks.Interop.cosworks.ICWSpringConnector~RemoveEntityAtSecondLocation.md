---
title: "RemoveEntityAtSecondLocation Method (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "RemoveEntityAtSecondLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RemoveEntityAtSecondLocation.html"
---

# RemoveEntityAtSecondLocation Method (ICWSpringConnector)

Removes the entity at the specified location from the second location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntityAtSecondLocation( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
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

- `NIndex`: 0-based index at which to remove entity

## VBA Syntax

See [CWSpringConnector::RemoveEntityAtSecondLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~RemoveEntityAtSecondLocation.html).

## Remarks

Before calling this method, call [ICWSpringConnector::GetTargetEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSpringConnector~GetTargetEntityCount.html) to determine the value of NIndex.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
