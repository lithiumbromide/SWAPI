---
title: "ResumeSelectionList Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "ResumeSelectionList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList.html"
---

# ResumeSelectionList Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::ResumeSelectionList2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ResumeSelectionList()
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr

instance.ResumeSelectionList()
```

### C#

```csharp
void ResumeSelectionList()
```

### C++/CLI

```cpp
void ResumeSelectionList();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SelectionMgr::ResumeSelectionList](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~ResumeSelectionList.html).

## Examples

[Get Objects in Selection List (C#)](Get_Objects_in_Selection_Set_Example_CSharp.htm)
[Get Objects in Selection List (VB.NET)](Get_Objects_in_Selection_Set_Example_VBNET.htm)
[Get Objects in Selection List (VBA)](Get_Objects_in_Selection_Set_Example_VB.htm)

## Remarks

To add objects to a selection list without preselecting the objects in the user interface:

1. Call [ISelectionMgr::SuspendSelectionList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~SuspendSelectionList.html) to suspend the current selection list, preserving its contents and starting a new selection list.
2. To populate a new selection list, call [ISelectionMgr::AddSelectionListObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObject.html) or [ISelectionMgr::AddSelectionListObjects](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.html).

  **NOTE**: To add objects in a [selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html) in a new selection list, call [ISelectionSet::Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~Select.html).
3. Process the objects in the new selection list.
4. Call ISelectionMgr::ResumeSelectionList to reinstate the suspended selection list.

To programmatically preselect objects in the user interface and add them to a selection list, use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
