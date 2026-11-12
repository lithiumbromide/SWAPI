---
title: "InsertEntityAtFirstLocation Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "InsertEntityAtFirstLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertEntityAtFirstLocation.html"
---

# InsertEntityAtFirstLocation Method (ICWBoltConnector)

Inserts a source entity at the first location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntityAtFirstLocation( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim DispEntity As System.Object

instance.InsertEntityAtFirstLocation(DispEntity)
```

### C#

```csharp
void InsertEntityAtFirstLocation(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertEntityAtFirstLocation(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Source entity (face or edge depending on the type of bolt connector)

## VBA Syntax

See [CWBoltConnector::InsertEntityAtFirstLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~InsertEntityAtFirstLocation.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::InsertEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertEntityAtSecondLocation.html)
[ICWBoltConnector::RemoveEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveEntityAtFirstLocation.html)
[ICWBoltConnector::RemoveEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveEntityAtSecondLocation.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
