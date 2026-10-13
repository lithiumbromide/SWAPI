---
title: "InsertEntityAtSecondLocation Method (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "InsertEntityAtSecondLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~InsertEntityAtSecondLocation.html"
---

# InsertEntityAtSecondLocation Method (ICWSpringConnector)

Inserts an entity at the second location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntityAtSecondLocation( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim DispEntity As System.Object

instance.InsertEntityAtSecondLocation(DispEntity)
```

### C#

```csharp
void InsertEntityAtSecondLocation(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertEntityAtSecondLocation(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Entity

## VBA Syntax

See [CWSpringConnector::InsertEntityAtSecondLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~InsertEntityAtSecondLocation.html).

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringLocation::RemoveEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RemoveEntityAtSecondLocation.html)
[ICWSpringLocation::RemoveEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~RemoveEntityAtFirstLocation.html)
[ICWSpringLocation::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~InsertEntityAtFirstLocation.html)
[ICWSpringConnector::GetTargetEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~GetTargetEntityCount.html)
[ICWSpringConnector::GetSourceEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~GetSourceEntityCount.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
