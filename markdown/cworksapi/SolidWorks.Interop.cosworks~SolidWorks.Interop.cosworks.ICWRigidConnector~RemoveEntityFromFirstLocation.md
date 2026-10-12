---
title: "RemoveEntityFromFirstLocation Method (ICWRigidConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRigidConnector"
member: "RemoveEntityFromFirstLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromFirstLocation.html"
---

# RemoveEntityFromFirstLocation Method (ICWRigidConnector)

Removes the specified entity from the first location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntityFromFirstLocation( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRigidConnector
Dim NIndex As System.Integer

instance.RemoveEntityFromFirstLocation(NIndex)
```

### C#

```csharp
void RemoveEntityFromFirstLocation(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveEntityFromFirstLocation(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index at which to remove entity

## VBA Syntax

See [CWRigidConnector::RemoveEntityFromFirstLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRigidConnector~RemoveEntityFromFirstLocation.html).

## See Also

[ICWRigidConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector.html)
[ICWRigidConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector_members.html)
[ICWRigidConnector::GetFirstLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetFirstLocationEntityCount.html)
[ICWRigidConnector::GetSecondLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetSecondLocationEntityCount.html)
[ICWRigidConnector::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtFirstLocation.html)
[ICWRigidConnector::InsertEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtSecondLocation.html)
[ICWRigidConnector::RemoveEntityFromSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromSecondLocation.html)

## Availability

SOLIDWORKS Simulation 2009 SP0
