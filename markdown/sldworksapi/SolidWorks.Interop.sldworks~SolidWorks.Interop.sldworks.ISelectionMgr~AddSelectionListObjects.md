---
title: "AddSelectionListObjects Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "AddSelectionListObjects"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.html"
---

# AddSelectionListObjects Method (ISelectionMgr)

Adds the specified objects to the selection list.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSelectionListObjects( _
   ByVal Objects As System.Object, _
   ByVal SelectData As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Objects As System.Object
Dim SelectData As System.Object
Dim value As System.Integer

value = instance.AddSelectionListObjects(Objects, SelectData)
```

### C#

```csharp
System.int AddSelectionListObjects(
   System.object Objects,
   System.object SelectData
)
```

### C++/CLI

```cpp
System.int AddSelectionListObjects(
   System.Object^ Objects,
   System.Object^ SelectData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Objects`: Array of objects to add to the selection list (see **Remarks**)
- `SelectData`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html)

### Return Value

Number of objects added to the selection list

## VBA Syntax

See [SelectionMgr::AddSelectionListObjects](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~AddSelectionListObjects.html).

## Examples

[Add Objects to Selection List (VBA)](Add_Objects_to_Selection_List_Example_VB.htm)
[Add Objects to Selection List (VB.NET)](Add_Objects_to_Selection_List_Example_VBNET.htm)
[Add Objects to Selection List (C#)](Add_Objects_to_Selection_List_Example_CSharp.htm)

## Remarks

For VB.NET and C# applications, specify Objects as an array of System.Runtime.InteropServices.DispatchWrappers. See the examples and [IDispatch Object Arrays as Input in .NET](sldworksapiprogguide.chm::/OVERVIEW/IDispatch_Object_Arrays_as_Input_in_.NET.htm) for more information.

Call [ISelectionMgr::CreateSelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~CreateSelectData.html) to specify SelectData.

To add objects to a selection list without preselecting the objects in the user interface:

1. Call [ISelectionMgr::SuspendSelectionList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~SuspendSelectionList.html) to suspend the current selection list, preserving its contents and starting a new selection list.
2. Call [ISelectionMgr::AddSelectionListObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObject.html) or ISelectionMgr::AddSelectionListObjects to populate a new selection list.
3. Process the objects in the new selection list.
4. Call [ISelectionMgr::ResumeSelectionList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~ResumeSelectionList.html) to reinstate the suspended selection list.

To programmatically preselect objects in the user interface and add them to a selection list, use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionSetItem::GetCorrespondingItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem~GetCorrespondingItem.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
