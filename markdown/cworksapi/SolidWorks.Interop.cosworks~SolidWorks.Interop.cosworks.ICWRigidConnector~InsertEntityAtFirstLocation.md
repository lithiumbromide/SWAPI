---
title: "InsertEntityAtFirstLocation Method (ICWRigidConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRigidConnector"
member: "InsertEntityAtFirstLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtFirstLocation.html"
---

# InsertEntityAtFirstLocation Method (ICWRigidConnector)

Inserts entity at the first location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntityAtFirstLocation( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRigidConnector
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

- `DispEntity`: Entity

## VBA Syntax

See [CWRigidConnector::InsertEntityAtFirstLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRigidConnector~InsertEntityAtFirstLocation.html).

## See Also

[ICWRigidConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector.html)
[ICWRigidConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector_members.html)
[ICWRigidConnector::GetFirstLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetFirstLocationEntityCount.html)
[ICWRigidConnector::GetSecondLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetSecondLocationEntityCount.html)
[ICWRigidConnector::InsertEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtSecondLocation.html)
[ICWRigidConnector::RemoveEntityFromFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromFirstLocation.html)
[ICWRigidConnector::RemoveEntityFromSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromSecondLocation.html)

## Availability

SOLIDWORKS Simulation 2009 SP0
