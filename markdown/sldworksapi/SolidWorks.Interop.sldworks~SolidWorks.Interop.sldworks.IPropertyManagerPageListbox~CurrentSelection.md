---
title: "CurrentSelection Property (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "CurrentSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~CurrentSelection.html"
---

# CurrentSelection Property (IPropertyManagerPageListbox)

Gets and sets the item that is currently selected in this list box.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentSelection As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
Dim value As System.Short

instance.CurrentSelection = value

value = instance.CurrentSelection
```

### C#

```csharp
System.short CurrentSelection {get; set;}
```

### C++/CLI

```cpp
property System.short CurrentSelection {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Index number of the item in the 0-based list

## VBA Syntax

See [PropertyManagerPageListbox::CurrentSelection](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageListbox~CurrentSelection.html).

## Remarks

If you use this property with a list box enabled for [multiple selections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageListbox~Style.html), then this method returns -1 and does not affect the list box.

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
