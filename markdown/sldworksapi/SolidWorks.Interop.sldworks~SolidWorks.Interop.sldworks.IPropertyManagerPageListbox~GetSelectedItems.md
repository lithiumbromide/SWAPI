---
title: "GetSelectedItems Method (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "GetSelectedItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItems.html"
---

# GetSelectedItems Method (IPropertyManagerPageListbox)

Gets the items selected in a list box enabled for multiple selections.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedItems() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
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

Array of shorts of the currently selected items in this list box

## VBA Syntax

See [PropertyManagerPageListbox::GetSelectedItems](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageListbox~GetSelectedItems.html).

## Remarks

Each item is a 0-based index into the list of items.

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)
[IPropertyManagerPageListbox::IGetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~IGetSelectedItems.html)
[IPropertyManagerPageListbox::GetSelectedItemsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItemsCount.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
