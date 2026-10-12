---
title: "ItemText Property (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "ItemText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~ItemText.html"
---

# ItemText Property (IPropertyManagerPageListbox)

Gets the text for the specified item in this list box.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ItemText( _
   ByVal Item As System.Short _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
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

- `Item`: Position of the item where to get the text in the 0-based list or -1 to get the text of the currently selected item

### Property Value

Text for the specified item

## VBA Syntax

See [PropertyManagerPageListbox::ItemText](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageListbox~ItemText.html).

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
