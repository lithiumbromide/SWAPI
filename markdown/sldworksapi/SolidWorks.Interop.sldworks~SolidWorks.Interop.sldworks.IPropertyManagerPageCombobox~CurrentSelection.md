---
title: "CurrentSelection Property (IPropertyManagerPageCombobox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCombobox"
member: "CurrentSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~CurrentSelection.html"
---

# CurrentSelection Property (IPropertyManagerPageCombobox)

Gets and sets the item that is currently selected for this combo box.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentSelection As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageCombobox
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

Index number of the currently selected item in the 0-based list of items

## VBA Syntax

See [PropertyManagerPageCombobox::CurrentSelection](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageCombobox~CurrentSelection.html).

## Examples

See the [IPropertyManagerPageCombobox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html) examples.

## See Also

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html)
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
