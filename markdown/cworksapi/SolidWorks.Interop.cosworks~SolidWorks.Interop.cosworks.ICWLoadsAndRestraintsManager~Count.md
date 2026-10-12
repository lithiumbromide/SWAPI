---
title: "Count Property (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "Count"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~Count.html"
---

# Count Property (ICWLoadsAndRestraintsManager)

Gets the number of loads and restraints defined in the active study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Count As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim value As System.Integer

value = instance.Count
```

### C#

```csharp
System.int Count {get;}
```

### C++/CLI

```cpp
property System.int Count {
   System.int get();
}
```

### Property Value

Number of loads and restraints

## VBA Syntax

See [CWLoadsAndRestraintsManager::Count](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~Count.html).

## Examples

[Copy Items to Another Study (VBA)](Copy_Items_to_Another_Study_Example_VB.htm)
[Copy Items to Another Study (VB.NET)](Copy_Items_to_Another_Study_Example_VBNET.htm)
[Copy Items to Another Study (C#)](Copy_Items_to_Another_Study_Example_CSharp.htm)

## Remarks

Call this method before calling [ICWLoadsAndRestraintsManager::GetLoadsAndRestraints](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager~GetLoadsAndRestraints.html).

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::GetEdgeWeldConnector Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetEdgeWeldConnector.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
