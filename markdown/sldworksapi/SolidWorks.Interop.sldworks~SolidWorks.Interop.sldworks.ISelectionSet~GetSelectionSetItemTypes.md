---
title: "GetSelectionSetItemTypes Method (ISelectionSet)"
project: "SOLIDWORKS API Help"
interface: "ISelectionSet"
member: "GetSelectionSetItemTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItemTypes.html"
---

# GetSelectionSetItemTypes Method (ISelectionSet)

Gets the types of entities in this selection set.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionSetItemTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionSet
Dim value As System.Object

value = instance.GetSelectionSetItemTypes()
```

### C#

```csharp
System.object GetSelectionSetItemTypes()
```

### C++/CLI

```cpp
System.Object^ GetSelectionSetItemTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of longs or integers of the types of entities in this selection set as defined in [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html) (see **Remarks**)

## VBA Syntax

See [SelectionSet::GetSelectionSetItemTypes](ms-its:sldworksapivb6.chm::/sldworks~SelectionSet~GetSelectionSetItemTypes.html).

## Examples

[Create and Delete Selection Sets (C#)](Create_and_Delete_Selection_Sets_Example_CSharp.htm)
[Create and Delete Selection Sets (VB.NET)](Create_and_Delete_Selection_Sets_Example_VBNET.htm)
[Create and Delete Selection Sets (VBA)](Create_and_Delete_Selection_Sets_Example_VB.htm)
[Get Dispatch Objects for Selection Set Items (C#)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_CSharp.htm)
[Get Dispatch Objects for Selection Set Items (VB.NET)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VBNET.htm)
[Get Dispatch Objects for Selection Set Items (VBA)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VB.htm)

## Remarks

The order of the array of the types of entities returned by this method matches the order of the array of selection set items returned by [ISelectionSet::GetSelectionSetItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItems.html).

## See Also

[ISelectionSet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html)
[ISelectionSet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet_members.html)
[ISelectionSetItem::GetCorrespondingItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem~GetCorrespondingItem.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
