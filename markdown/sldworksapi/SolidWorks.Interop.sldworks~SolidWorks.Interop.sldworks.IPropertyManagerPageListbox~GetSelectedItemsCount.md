---
title: "GetSelectedItemsCount Method (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "GetSelectedItemsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItemsCount.html"
---

# GetSelectedItemsCount Method (IPropertyManagerPageListbox)

Gets the number of items currently selected in a list box enabled for multiple selection.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedItemsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
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

Number of items currently selected in this list box

## VBA Syntax

See [PropertyManagerPageListbox::GetSelectedItemsCount](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageListbox~GetSelectedItemsCount.html).

## Remarks

Call this method before calling [IPropertyManagerPageListbox::IGetSelectedItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageListbox~IGetSelectedItems.html) to size the array of selected items.

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)
[IPropertyManagerPageListbox::GetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItems.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
