---
title: "CopyLoadsAndRestraintsToStudy Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "CopyLoadsAndRestraintsToStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~CopyLoadsAndRestraintsToStudy.html"
---

# CopyLoadsAndRestraintsToStudy Method (ICWLoadsAndRestraintsManager)

Copies the specified loads and restraints to the specified study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CopyLoadsAndRestraintsToStudy( _
   ByVal SStudyName As System.String, _
   ByVal LRNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim SStudyName As System.String
Dim LRNames As System.Object
Dim value As System.Integer

value = instance.CopyLoadsAndRestraintsToStudy(SStudyName, LRNames)
```

### C#

```csharp
System.int CopyLoadsAndRestraintsToStudy(
   System.string SStudyName,
   System.object LRNames
)
```

### C++/CLI

```cpp
System.int CopyLoadsAndRestraintsToStudy(
   System.String^ SStudyName,
   System.Object^ LRNames
)
```

### Parameters

- `SStudyName`: Name of study to which to copy loads and restraints
- `LRNames`: Array of names of loads and restraints to copy (see **Remarks**)

### Return Value

Error code as defined in [swsCopyItemsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCopyItemsError_e.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::CopyLoadsAndRestraintsToStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~CopyLoadsAndRestraintsToStudy.html).

## Examples

[Copy Items to Another Study (VBA)](Copy_Items_to_Another_Study_Example_VB.htm)
[Copy Items to Another Study (VB.NET)](Copy_Items_to_Another_Study_Example_VBNET.htm)
[Copy Items to Another Study (C#)](Copy_Items_to_Another_Study_Example_CSharp.htm)

## Remarks

To populate the array of LRNames, either:

- inspect the Simulation study tree.

- or -

- call [ICWLoadsAndRestraintsManager::GetLoadsAndRestraints](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetLoadsAndRestraints.html) to get each [ICWLoadsAndRestraints](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html) and then call [ICWLoadsAndRestraints::Name](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints~Name.html) to get the name of each load or restraint.

If a load or restraint name already exists, **Copy[1]** is prepended to the name of the copied load or restraint.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::DeleteLoadsAndRestraints Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~DeleteLoadsAndRestraints.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
