---
title: "RemoveEntityFromSecondLocation Method (ICWRigidConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRigidConnector"
member: "RemoveEntityFromSecondLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromSecondLocation.html"
---

# RemoveEntityFromSecondLocation Method (ICWRigidConnector)

Removes the specified entity from the second location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntityFromSecondLocation( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRigidConnector
Dim NIndex As System.Integer

instance.RemoveEntityFromSecondLocation(NIndex)
```

### C#

```csharp
void RemoveEntityFromSecondLocation(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveEntityFromSecondLocation(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index at which to remove entity

## VBA Syntax

See [CWRigidConnector::RemoveEntityFromSecondLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRigidConnector~RemoveEntityFromSecondLocation.html).

## See Also

[ICWRigidConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector.html)
[ICWRigidConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector_members.html)
[ICWRigidConnector::GetFirstLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetFirstLocationEntityCount.html)
[ICWRigidConnector::GetSecondLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetSecondLocationEntityCount.html)
[ICWRigidConnector::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtFirstLocation.html)
[ICWRigidConnector::InsertEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtSecondLocation.html)
[ICWRigidConnector::RemoveEntityFromFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromFirstLocation.html)

## Availability

SOLIDWORKS Simulation 2009 SP0
