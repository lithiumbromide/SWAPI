---
title: "GetSelectedItems Method (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "GetSelectedItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItems.html"
---

# GetSelectedItems Method (IPropertyManagerPageSelectionbox)

Gets the items selected in a PropertyManager selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedItems() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Object

value = instance.GetSelectedItems()
```

### C#

```csharp
System.object GetSelectedItems()
```

### C++/CLI

```cpp
System.Object^ GetSelectedItems();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of shorts of the indices of the currently selected items

## VBA Syntax

See [IPropertyManagerPageSelectionbox::GetSelectedItems](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageSelectionbox~GetSelectedItems.html).

## Remarks

Each item is a 0-based index into the list of items. For example, if there are five (5) items in the selection box and the first and last items are selected, then this method will return an array containing 0, 4.

Before calling this method, call [IPropertyManagerPageSelectionbox::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageNumberbox~Style.html) and set the style to swPropMgrPageSelectionBoxStyle_MultipleItemSelect to enable multiple selections.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)
[IPropertyManagerPageSelectionbox::IGetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~IGetSelectedItems.html)
[IPropertyManagerPageSelectionbox::GetSelectedItemsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItemsCount.html)
[IPropertyManagerPageSelectionbox::SetSelectedItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetSelectedItem.html)
[IPropertyManagerPageSelectionbox::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Style.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
