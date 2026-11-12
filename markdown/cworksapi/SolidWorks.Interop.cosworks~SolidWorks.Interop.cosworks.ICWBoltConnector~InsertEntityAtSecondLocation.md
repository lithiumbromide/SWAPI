---
title: "InsertEntityAtSecondLocation Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "InsertEntityAtSecondLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertEntityAtSecondLocation.html"
---

# InsertEntityAtSecondLocation Method (ICWBoltConnector)

Inserts a target entity at the second location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntityAtSecondLocation( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
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

- `DispEntity`: Target entity (face, edge, or plane depending on the type of bolt connector)

## VBA Syntax

See [CWBoltConnector::InsertEntityAtSecondLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~InsertEntityAtSecondLocation.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertEntityAtFirstLocation.html)
[ICWBoltConnector::RemoveEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveEntityAtSecondLocation.html)
[ICWBoltConnector::RemoveEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveEntityAtFirstLocation.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
