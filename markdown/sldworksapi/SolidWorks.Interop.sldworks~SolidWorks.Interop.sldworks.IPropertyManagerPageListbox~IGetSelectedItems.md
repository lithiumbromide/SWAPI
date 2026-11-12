---
title: "IGetSelectedItems Method (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "IGetSelectedItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~IGetSelectedItems.html"
---

# IGetSelectedItems Method (IPropertyManagerPageListbox)

Gets the items selected in a list box enabled for multiple selections.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelectedItems( _
   ByVal Count As System.Integer _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
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

- `Count`: Number of selected items

### Return Value

- in-process, unmanaged C++: Pointer to an array of shorts of the currently selected items in this list box

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Each item is a 0-based index into the list of items.

Call [IPropertyManagerPageListbox::GetSelectedItemsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItemsCount.html) to size the returned array.

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)
[IPropertyManagerPageListbox::GetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItems.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
