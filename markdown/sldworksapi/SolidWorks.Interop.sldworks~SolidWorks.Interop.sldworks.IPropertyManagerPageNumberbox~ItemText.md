---
title: "ItemText Property (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "ItemText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~ItemText.html"
---

# ItemText Property (IPropertyManagerPageNumberbox)

Gets the text for an item in the attached drop-down list for this number box.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ItemText( _
   ByVal Item As System.Short _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
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

Text for this item

## VBA Syntax

See [PropertyManagerPageNumberbox::ItemText](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageNumberbox~ItemText.html).

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
