---
title: "CurrentSelection Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "CurrentSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~CurrentSelection.html"
---

# CurrentSelection Property (IPropertyManagerPageSelectionbox)

Gets or sets the index number of the currently selected item in this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentSelection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer

instance.CurrentSelection = value

value = instance.CurrentSelection
```

### C#

```csharp
System.int CurrentSelection {get; set;}
```

### C++/CLI

```cpp
property System.int CurrentSelection {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0-based index of the currently selected item in this selection box

## VBA Syntax

See [PropertyManagerPageSelectionbox::CurrentSelection](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~CurrentSelection.html).

## Remarks

The return value Item is the item in the selection box that is selected. Only the active selection box can have a current selection. If you use this property with an inactive selection box, -1 is returned. See [IPropertyManagerPageSelectionbox::GetSelectionFocus](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectionFocus.html) to determine if a selection box is active or not.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
