---
title: "GetCorrespondingItem Method (ISelectionSetItem)"
project: "SOLIDWORKS API Help"
interface: "ISelectionSetItem"
member: "GetCorrespondingItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem~GetCorrespondingItem.html"
---

# GetCorrespondingItem Method (ISelectionSetItem)

Gets the Dispatch object for this selection set item.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorrespondingItem() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionSetItem
Dim value As System.Object

value = instance.GetCorrespondingItem()
```

### C#

```csharp
System.object GetCorrespondingItem()
```

### C++/CLI

```cpp
System.Object^ GetCorrespondingItem();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the Dispatch object for this selection set item (see **Remarks**)

## VBA Syntax

See [SelectionSetItem::GetCorrespondingItem](ms-its:sldworksapivb6.chm::/sldworks~SelectionSetItem~GetCorrespondingItem.html).

## Examples

[Get Dispatch Objects for Selection Set Items (C#)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_CSharp.htm)
[Get Dispatch Objects for Selection Set Items (VB.NET)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VBNET.htm)
[Get Dispatch Objects for Selection Set Items (VBA)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VB.htm)

## Remarks

You can use this method to:

- pass the Dispatch object to [ISelectionMgr::AddSelectionListObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject.html) or [ISelectionMgr::AddSelectionListObjects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.html).
- typecast each element in [an array containing selection set item types](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItemTypes.html). See the examples.

## See Also

[ISelectionSetItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem.html)
[ISelectionSetItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
