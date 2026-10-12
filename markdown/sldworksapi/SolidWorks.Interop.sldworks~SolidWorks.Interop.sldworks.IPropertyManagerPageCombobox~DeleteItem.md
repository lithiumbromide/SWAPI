---
title: "DeleteItem Method (IPropertyManagerPageCombobox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCombobox"
member: "DeleteItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~DeleteItem.html"
---

# DeleteItem Method (IPropertyManagerPageCombobox)

Deletes an item from the attached drop-down list of this combo box.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteItem( _
   ByVal Item As System.Short _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageCombobox
Dim Item As System.Short
Dim value As System.Short

value = instance.DeleteItem(Item)
```

### C#

```csharp
System.short DeleteItem(
   System.short Item
)
```

### C++/CLI

```cpp
System.short DeleteItem(
   System.short Item
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Item`: Index number of the item to delete from the 0-based list of items

### Return Value

Number of items remaining in the list or -1 if the item is not deleted

## VBA Syntax

See [PropertyManagerPageCombobox::DeleteItem](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageCombobox~DeleteItem.html).

## See Also

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html)
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
