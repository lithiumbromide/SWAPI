---
title: "ItemCount Property (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "ItemCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~ItemCount.html"
---

# ItemCount Property (IPropertyManagerPageListbox)

Gets the number of items in the attached drop-down list for this list box.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ItemCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
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

Number of items in the attached drop-down list for this list box

## VBA Syntax

See [PropertyManagerPageListbox::ItemCount](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageListbox~ItemCount.html).

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
