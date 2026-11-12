---
title: "GetSelectionSetItems Method (ISelectionSet)"
project: "SOLIDWORKS API Help"
interface: "ISelectionSet"
member: "GetSelectionSetItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItems.html"
---

# GetSelectionSetItems Method (ISelectionSet)

Gets the selection set items in this selection set.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionSetItems() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionSet
Dim value As System.Object

value = instance.GetSelectionSetItems()
```

### C#

```csharp
System.object GetSelectionSetItems()
```

### C++/CLI

```cpp
System.Object^ GetSelectionSetItems();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [selection set items](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem.html)

## VBA Syntax

See [SelectionSet::GetSelectionSetItems](ms-its:sldworksapivb6.chm::/sldworks~SelectionSet~GetSelectionSetItems.html).

## Examples

[Create and Delete Selection Sets (C#)](Create_and_Delete_Selection_Sets_Example_CSharp.htm)
[Create and Delete Selection Sets (VB.NET)](Create_and_Delete_Selection_Sets_Example_VBNET.htm)
[Create and Delete Selection Sets (VBA)](Create_and_Delete_Selection_Sets_Example_VB.htm)
[Get Dispatch Objects for Selection Set Items (C#)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_CSharp.htm)
[Get Dispatch Objects for Selection Set Items (VB.NET)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VBNET.htm)
[Get Dispatch Objects for Selection Set Items (VBA)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VB.htm)

## Remarks

To get the types of entities in the selection set, call [ISelectionSet::GetSelectionSetItemTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItemTypes.html).

## See Also

[ISelectionSet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html)
[ISelectionSet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
