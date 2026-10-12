---
title: "GetSecondLocationEntityCount Method (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "GetSecondLocationEntityCount"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~GetSecondLocationEntityCount.html"
---

# GetSecondLocationEntityCount Method (ICWPinConnector)

Gets the number of entities at the second location.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSecondLocationEntityCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Integer

value = instance.GetSecondLocationEntityCount()
```

### C#

```csharp
System.int GetSecondLocationEntityCount()
```

### C++/CLI

```cpp
System.int GetSecondLocationEntityCount();
```

### Return Value

Number of entities at the second location

## VBA Syntax

See [CWPinConnector::GetSecondLocationEntityCountl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~GetSecondLocationEntityCount.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::GetFirstLocationEntityCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~GetFirstLocationEntityCount.html)
[ICWPinConnector::InsertEntityAtFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtFirstLocation.html)
[ICWPinConnector::InsertEntityAtSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~InsertEntityAtSecondLocation.html)
[ICWPinConnector::RemoveEntityFromFirstLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromFirstLocation.html)
[ICWPinConnector::RemoveEntityFromSecondLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRigidConnector~RemoveEntityFromSecondLocation.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
