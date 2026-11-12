---
title: "SuspendSelectionList Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "SuspendSelectionList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList.html"
---

# SuspendSelectionList Method (ISelectionMgr)

Suspends the current selection list.

## Syntax

### Visual Basic (Declaration)

```vb
Function SuspendSelectionList() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim value As System.Integer

value = instance.SuspendSelectionList()
```

### C#

```csharp
System.int SuspendSelectionList()
```

### C++/CLI

```cpp
System.int SuspendSelectionList();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

0 if the suspended list is empty, 1 if not

## VBA Syntax

See [SelectionMgr::SuspendSelectionList](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~SuspendSelectionList.html).

## Examples

[Add Objects to Selection List (C#)](Add_Objects_to_Selection_List_Example_CSharp.htm)
[Add Objects to Selection List (VB.NET)](Add_Objects_to_Selection_List_Example_VBNET.htm)
[Add Objects to Selection List (VBA)](Add_Objects_to_Selection_List_Example_VB.htm)
[Get Objects in Selection List (C#)](Get_Objects_in_Selection_Set_Example_CSharp.htm)
[Get Objects in Selection List (VB.NET)](Get_Objects_in_Selection_Set_Example_VBNET.htm)
[Get Objects in Selection List (VBA)](Get_Objects_in_Selection_Set_Example_VB.htm)

## Remarks

To add objects to a selection list without preselecting the objects in the user interface:

1. Call ISelectionMgr::SuspendSelectionList to suspend the current selection list, preserving its contents and starting a new selection list.
2. To populate a new selection list, call [ISelectionMgr::AddSelectionListObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObject.html) or [ISelectionMgr::AddSelectionListObjects](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.html).

  **NOTE**: To add objects in a [selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html) to a new selection list, call [ISelectionSet::Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~Select.html).
3. Call [ISelectionMgr::ResumeSelectionList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~ResumeSelectionList.html) to reinstate the suspended selection list.

To programmatically preselect objects in the user interface and add them to a selection list, use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

[IModelDoc2::ClearSelection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ClearSelection2.html) works like ISelectionMgr::SuspendSelectionList to clear the selection list. Unlike IModelDoc2::ClearSelection2, this method preserves the list for future reinstatement.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
