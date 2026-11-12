---
title: "InsertItem Method (IPropertyManagerPageCombobox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCombobox"
member: "InsertItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~InsertItem.html"
---

# InsertItem Method (IPropertyManagerPageCombobox)

Inserts an item in the attached drop-down list of this combo box.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertItem( _
   ByVal Item As System.Short, _
   ByVal Text As System.String _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageCombobox
Dim Item As System.Short
Dim Text As System.String
Dim value As System.Short

value = instance.InsertItem(Item, Text)
```

### C#

```csharp
System.short InsertItem(
   System.short Item,
   System.string Text
)
```

### C++/CLI

```cpp
System.short InsertItem(
   System.short Item,
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Item`: Position where to add the item in the 0-based list or -1 to put the item at the end of the list
- `Text`: Text for item

### Return Value

Position in the 0-based list where the item is added or -1 if the item is not added to the list

## VBA Syntax

See [PropertyManagerPageCombobox::InsertItem](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageCombobox~InsertItem.html).

## See Also

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html)
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
