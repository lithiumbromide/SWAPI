---
title: "SetSelectedItem Method (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "SetSelectedItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~SetSelectedItem.html"
---

# SetSelectedItem Method (IPropertyManagerPageListbox)

Sets whether an item is selected or cleared in a list box enabled for multiple selection.

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
Dim instance As IPropertyManagerPageListbox
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
- `Selected`: True to select the item, false to not

### Return Value

True if the item was selected or cleared, false if not

## VBA Syntax

See [PropertyManagerPageListbox::SetSelectedItem](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageListbox~SetSelectedItem.html).

## Examples

See the [IPropertyManagerPageListbox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html) examples.

## Remarks

The value specified for Item must be a valid index number. If it is not, then this method returns false. Thus, set up your list item index before using this method.

If you use this method to set a selected item in a single-selection style list box and another item in the list box is already selected, then that item is automatically cleared. You can use this method to clear a selection in a single-selection style list box, which results in no current selection in that list box.

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
