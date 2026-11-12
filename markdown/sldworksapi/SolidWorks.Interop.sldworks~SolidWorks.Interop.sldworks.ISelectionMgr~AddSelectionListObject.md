---
title: "AddSelectionListObject Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "AddSelectionListObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject.html"
---

# AddSelectionListObject Method (ISelectionMgr)

Adds the specified object to the selection list.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSelectionListObject( _
   ByVal Object As System.Object, _
   ByVal SelectData As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Object As System.Object
Dim SelectData As System.Object
Dim value As System.Boolean

value = instance.AddSelectionListObject(Object, SelectData)
```

### C#

```csharp
System.bool AddSelectionListObject(
   System.object Object,
   System.object SelectData
)
```

### C++/CLI

```cpp
System.bool AddSelectionListObject(
   System.Object^ Object,
   System.Object^ SelectData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Object`: Object to add to the selection list (see **Remarks**)
- `SelectData`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html)

### Return Value

True if successful, false if not

## VBA Syntax

See [SelectionMgr::AddSelectionListObject](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~AddSelectionListObject.html).

## Examples

[Insert Indent Feature (C#)](Insert_Indent_Feature_Example_CSharp.htm)
[Insert Indent Feature (VB.NET)](Insert_Indent_Feature_Example_VBNET.htm)
[Insert Indent Feature (VBA)](Insert_Indent_Feature_Example_VB.htm)

## Remarks

Call [ISelectionMgr::CreateSelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~CreateSelectData.html) to specify SelectData.

To add objects to a selection list without pre-selecting the objects in the user interface:

1. Call [ISelectionMgr::SuspendSelectionList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~SuspendSelectionList.html) to suspend the current selection list, preserving its contents and starting a new selection list.
2. Call ISelectionMgr::AddSelectionListObject or [ISelectionMgr::AddSelectionListObjects](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.html) to populate the new selection list.
3. Process the objects in the new selection list.
4. Call [ISelectionMgr::ResumeSelectionList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~ResumeSelectionList.html) to reinstate the suspended selection list.

To programmatically pre-select objects in the user interface and add them to a selection list, use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionSetItem::GetCorrespondingItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem~GetCorrespondingItem.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
