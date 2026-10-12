---
title: "IGetSelectedItems Method (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "IGetSelectedItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~IGetSelectedItems.html"
---

# IGetSelectedItems Method (IPropertyManagerPageSelectionbox)

Gets the items selected in a PropertyManager selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelectedItems( _
   ByVal Count As System.Integer _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim Count As System.Integer
Dim value As System.Short

value = instance.IGetSelectedItems(Count)
```

### C#

```csharp
System.short IGetSelectedItems(
   System.int Count
)
```

### C++/CLI

```cpp
System.short IGetSelectedItems(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of items selected

### Return Value

- in-process, unmanaged C++: Pointer to an array of shorts of the indices of the currently selected items

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Each item is a 0-based index into the list of items. For example, if there are five (5) items in the selection box and the first and last items are selected, then this method will return an array containing 0, 4.

Before calling:

- this method, call [IPropertyManagerPageSelectionbox::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageNumberbox~Style.html) and set the style to swPropMgrPageSelectionBoxStyle_MultipleItemSelect to enable multiple selections.
- [IPropertyManagerPageSelectionbox::GetSelectedItemsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItemsCount.html) to ge the value of Count.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
