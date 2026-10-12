---
title: "ItemCount Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "ItemCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~ItemCount.html"
---

# ItemCount Property (IPropertyManagerPageSelectionbox)

Gets the number of items currently in this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ItemCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer

value = instance.ItemCount
```

### C#

```csharp
System.int ItemCount {get;}
```

### C++/CLI

```cpp
property System.int ItemCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of items currently in this selection box

## VBA Syntax

See [PropertyManagerPageSelectionbox::ItemCount](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~ItemCount.html).

## Remarks

Use this property before using [IPropertyManagerPageSelectionBox::SelectionIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~SelectionIndex.html).

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
