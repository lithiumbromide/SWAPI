---
title: "GetSelectedItemsCount Method (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "GetSelectedItemsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItemsCount.html"
---

# GetSelectedItemsCount Method (IPropertyManagerPageSelectionbox)

Gets the number of currently selected items in this PropertyManager selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedItemsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer

value = instance.GetSelectedItemsCount()
```

### C#

```csharp
System.int GetSelectedItemsCount()
```

### C++/CLI

```cpp
System.int GetSelectedItemsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of currently selected items

## VBA Syntax

See [PropertyManagerPageSelectionbox::GetSelectedItemsCount](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageSelectionbox~GetSelectedItemsCount.html).

## Remarks

Before calling:

- this method, call [IPropertyManagerPageSelectionbox::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~Style.html) and set the style to swPropMgrPageSelectionBoxStyle_MultipleItemSelect to enable multiple selections.
- [IPropertyManagerPageSelectionbox::IGetSelectedItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~IGetSelectedItems.html), call this method to get the size of the array for that method.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)
[IPropertyManagerPageSelectionbox::GetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItems.html)
[IPropertyManagerPageSelectionbox::SetSelectedItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetSelectedItem.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
