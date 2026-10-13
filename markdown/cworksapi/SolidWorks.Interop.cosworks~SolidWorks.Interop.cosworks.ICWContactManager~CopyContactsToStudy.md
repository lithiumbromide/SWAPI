---
title: "CopyContactsToStudy Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "CopyContactsToStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CopyContactsToStudy.html"
---

# CopyContactsToStudy Method (ICWContactManager)

Copies the specified contact sets to the specified study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CopyContactsToStudy( _
   ByVal SStudyName As System.String, _
   ByVal VarContactNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim SStudyName As System.String
Dim VarContactNames As System.Object
Dim value As System.Integer

value = instance.CopyContactsToStudy(SStudyName, VarContactNames)
```

### C#

```csharp
System.int CopyContactsToStudy(
   System.string SStudyName,
   System.object VarContactNames
)
```

### C++/CLI

```cpp
System.int CopyContactsToStudy(
   System.String^ SStudyName,
   System.Object^ VarContactNames
)
```

### Parameters

- `SStudyName`: Name of study to which to copy contact sets
- `VarContactNames`: Array of contact names (see **Remarks**)

### Return Value

Error code as defined in [swsCopyItemsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCopyItemsError_e.html)

## VBA Syntax

See [CWContactManager::CopyContactsToStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~CopyContactsToStudy.html).

## Examples

[Copy Items to Another Study (VBA)](Copy_Items_to_Another_Study_Example_VB.htm)
[Copy Items to Another Study (VB.NET)](Copy_Items_to_Another_Study_Example_VBNET.htm)
[Copy Items to Another Study (C#)](Copy_Items_to_Another_Study_Example_CSharp.htm)

## Remarks

To populate the array of VarContactNames, either:

- inspect **Connections > Contact Sets** in the Simulation study tree.

- or -

- call [ICWContactManager::GetContactSetAt](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~GetContactSetAt.html) to get each [ICWContactSet](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html) and then call [ICWContactSet::ContactName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactName.html) to get the name of each contact set.

If a contact set name already exists, **Copy[1]** is prepended to the name of the copied contact set.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
