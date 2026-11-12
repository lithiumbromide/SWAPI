---
title: "SelectionIndex Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "SelectionIndex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SelectionIndex.html"
---

# SelectionIndex Property (IPropertyManagerPageSelectionbox)

Gets the index number of the currently selected item in the selection box.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SelectionIndex( _
   ByVal Item As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim Item As System.Integer
Dim value As System.Integer

value = instance.SelectionIndex(Item)
```

### C#

```csharp
System.int SelectionIndex(
   System.int Item
) {get;}
```

### C++/CLI

```cpp
property System.int SelectionIndex {
   System.int get(System.int Item);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Item`: 0-based index number of the currently selected item (see **Remarks**)

### Property Value

1-based index number to use with [ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) APIs (see Remarks)

## VBA Syntax

See [PropertyManagerPageSelectionbox::SelectionIndex](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~SelectionIndex.html).

## Remarks

Use:

- [IPropertyManagerPageSelectionbox::ItemCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~ItemCount.html) to get the number of items in the selection box.
- the return value Index with such ISelectionMgr APIs as [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) and [ISelectionMgr::GetSelectedObjectType3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html).

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
