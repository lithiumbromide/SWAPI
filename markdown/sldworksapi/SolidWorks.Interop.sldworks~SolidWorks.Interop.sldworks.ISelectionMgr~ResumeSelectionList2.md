---
title: "ResumeSelectionList2 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "ResumeSelectionList2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList2.html"
---

# ResumeSelectionList2 Method (ISelectionMgr)

Reinstates the previously suspended selection list.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ResumeSelectionList2( _
   ByVal Append As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Append As System.Boolean

instance.ResumeSelectionList2(Append)
```

### C#

```csharp
void ResumeSelectionList2(
   System.bool Append
)
```

### C++/CLI

```cpp
void ResumeSelectionList2(
   System.bool Append
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True to append the new selection list to the suspended selection list and resume the combined selection list, false to just resume the suspended selection list

## VBA Syntax

See [SelectionMgr::ResumeSelectionList2](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~ResumeSelectionList2.html).

## Examples

[Add Objects to Selection List (VBA)](Add_Objects_to_Selection_List_Example_VB.htm)
[Add Objects to Selection List (VB.NET)](Add_Objects_to_Selection_List_Example_VBNET.htm)
[Add Objects to Selection List (C#)](Add_Objects_to_Selection_List_Example_CSharp.htm)

## Remarks

To add objects to a selection list without pre-selecting the objects in the user interface:

1. Call [ISelectionMgr::SuspendSelectionList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~SuspendSelectionList.html) to suspend the current selection list, preserving its contents and starting a new selection list.
2. To populate the new selection list, call [ISelectionMgr::AddSelectionListObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObject.html), [ISelectionMgr::AddSelectionListObjects](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.html), or [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html).

  **NOTE**: To add objects in a [selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html) to a new selection list, call [ISelectionSet::Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~Select.html).
3. Process the objects in the new selection list.
4. Call this method to reinstate the suspended selection list, setting Append to true to append the new selection list.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
