---
title: "InsertEntityAtSecondLocation Method (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "InsertEntityAtSecondLocation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~InsertEntityAtSecondLocation.html"
---

# InsertEntityAtSecondLocation Method (ICWPinConnector)

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
Dim instance As ICWPinConnector
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

See [CWPinConnector::InsertEntityAtSecondLocation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~InsertEntityAtSecondLocation.html).

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::GetFirstLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetFirstLocationEntityCount.html)
[ICWPinConnector::GetSecondLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetSecondLocationEntityCount.html)
[ICWPinConnector::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtFirstLocation.html)
[ICWPinConnector::RemoveEntityFromFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromFirstLocation.html)
[ICWPinConnector::RemoveEntityFromSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromSecondLocation.html)

## Availability

SOLIDWORKS Simulation 2009 SP0
