---
title: "SetSelectedItem Method (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "SetSelectedItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetSelectedItem.html"
---

# SetSelectedItem Method (IPropertyManagerPageSelectionbox)

Sets whether an item is selected or cleared in a [selection box enabled for multiple selection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~Style.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSelectedItem( _
   ByVal Item As System.Short, _
   ByVal Selected As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim Item As System.Short
Dim Selected As System.Boolean
Dim value As System.Boolean

value = instance.SetSelectedItem(Item, Selected)
```

### C#

```csharp
System.bool SetSelectedItem(
   System.short Item,
   System.bool Selected
)
```

### C++/CLI

```cpp
System.bool SetSelectedItem(
   System.short Item,
   System.bool Selected
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Item`: Index of the item to select or clear
- `Selected`: True to select the item, false to clear it

### Return Value

True if the time was selected or cleared, false if not

## VBA Syntax

See [PropertyManagerPageSelectionbox::SetSelectedItem](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageSelectionbox~SetSelectedItem.html).

## Remarks

The value specified for Item must be a valid index number. If it is not, then this method returns false. Thus, set up your list item index before using this method.

If you use this method to set a selected item in a single-selection style list box and another item in the list box is already selected, then that item is automatically cleared. You can use this method to clear a selection in a single-selection style list box, which results in no current selection in that list box.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)
[IPropertyManagerPageSelectionBox::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Style.html)
[IPropertyManagerPageSelectionBox::GetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItems.html)
[IPropertyManagerPageSelectionBox::IGetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~IGetSelectedItems.html)
[IPropertyManagerPageSelectionBox::GetSelectedItemsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItemsCount.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
