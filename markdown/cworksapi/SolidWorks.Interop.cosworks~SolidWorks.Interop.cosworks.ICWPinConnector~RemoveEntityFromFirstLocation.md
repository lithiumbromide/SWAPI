---
title: "RemoveEntityFromFirstLocation Method (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "RemoveEntityFromFirstLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~RemoveEntityFromFirstLocation.html"
---

# RemoveEntityFromFirstLocation Method (ICWPinConnector)

Removes the entity at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntityFromFirstLocation( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
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

- `NIndex`: Index of entity to remove

## VBA Syntax

See [CWPinConnector::RemoveEntityFromFirstLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~RemoveEntityFromFirstLocation.html).

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::GetFirstLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetFirstLocationEntityCount.html)
[ICWPinConnector::GetSecondLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetSecondLocationEntityCount.html)
[ICWPinConnector::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtFirstLocation.html)
[ICWPinConnector::InsertEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtSecondLocation.html)
[ICWPinConnector::RemoveEntityFromSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromSecondLocation.html)

## Availability

SOLIDWORKS Simulation 2009 SP0
