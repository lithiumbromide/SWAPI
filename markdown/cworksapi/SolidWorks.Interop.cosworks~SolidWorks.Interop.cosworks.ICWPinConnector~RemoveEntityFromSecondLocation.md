---
title: "RemoveEntityFromSecondLocation Method (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "RemoveEntityFromSecondLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~RemoveEntityFromSecondLocation.html"
---

# RemoveEntityFromSecondLocation Method (ICWPinConnector)

Removes the entity at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntityFromSecondLocation( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
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

- `NIndex`: Index of entity to remove

## VBA Syntax

See [CWPinConnector::RemoveEntityFromSecondLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~RemoveEntityFromSecondLocation.html).

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::GetFirstLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetFirstLocationEntityCount.html)
[ICWPinConnector::GetSecondLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetSecondLocationEntityCount.html)
[ICWPinConnector::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtFirstLocation.html)
[ICWPinConnector::InsertEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtSecondLocation.html)
[ICWPinConnector::RemoveEntityFromFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromFirstLocation.html)

## Availability

SOLIDWORKS Simulation 2009 SP0
