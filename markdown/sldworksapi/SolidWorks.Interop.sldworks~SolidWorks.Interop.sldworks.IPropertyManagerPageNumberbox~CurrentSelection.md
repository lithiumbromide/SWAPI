---
title: "CurrentSelection Property (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "CurrentSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~CurrentSelection.html"
---

# CurrentSelection Property (IPropertyManagerPageNumberbox)

Gets or sets the item that is currently selected in the number box.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentSelection As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
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

Index number of the item in the 0-based list of items

## VBA Syntax

See [PropertyManagerPageNumberbox::CurrentSelection](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageNumberbox~CurrentSelection.html).

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
