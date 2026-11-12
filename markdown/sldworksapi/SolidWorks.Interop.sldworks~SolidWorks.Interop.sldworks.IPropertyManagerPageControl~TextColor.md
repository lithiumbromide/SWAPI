---
title: "TextColor Property (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "TextColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~TextColor.html"
---

# TextColor Property (IPropertyManagerPageControl)

Gets or sets color of the text of a label on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim value As System.Integer

instance.TextColor = value

value = instance.TextColor
```

### C#

```csharp
System.int TextColor {get; set;}
```

### C++/CLI

```cpp
property System.int TextColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB color value for the text of a label on a PropertyManager page

## VBA Syntax

See [PropertyManagerPageControl::TextColor](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~TextColor.html).

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
