---
title: "Height Property (IPropertyManagerPageLabel)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageLabel"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Height.html"
---

# Height Property (IPropertyManagerPageLabel)

Gets or sets the height of this label.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageLabel
Dim value As System.Short

instance.Height = value

value = instance.Height
```

### C#

```csharp
System.short Height {get; set;}
```

### C++/CLI

```cpp
property System.short Height {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height of label in dialog box units; defaults to 8

## VBA Syntax

See [PropertyManagerPageLabel::Height](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageLabel~Height.html).

## Remarks

You can only set this property before the PropertyManager page is displayed.

Because SOLIDWORKS sizes the label appropriately based on the text it contains, you should not have to use this property. However, if the label does not contain text, then using this property might be useful.

## See Also

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
