---
title: "ItemText Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "ItemText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~ItemText.html"
---

# ItemText Property (IPropertyManagerPageSelectionbox)

Gets the specified item in this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ItemText( _
   ByVal Item As System.Short _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim Item As System.Short
Dim value As System.String

value = instance.ItemText(Item)
```

### C#

```csharp
System.string ItemText(
   System.short Item
) {get;}
```

### C++/CLI

```cpp
property System.String^ ItemText {
   System.String^ get(System.short Item);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Item`: Position of the item in the 0-based list; -1 to get the currently selected item

### Property Value

Text of the specified item

## VBA Syntax

See [PropertyManagerPageSelectionbox::ItemText](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~ItemText.html).

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
