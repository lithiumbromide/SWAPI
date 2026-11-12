---
title: "BackgroundColor Property (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "BackgroundColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~BackgroundColor.html"
---

# BackgroundColor Property (IPropertyManagerPageControl)

Gets or sets the background color of an edit box or label on the PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim value As System.Integer

instance.BackgroundColor = value

value = instance.BackgroundColor
```

### C#

```csharp
System.int BackgroundColor {get; set;}
```

### C++/CLI

```cpp
property System.int BackgroundColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB value for the color of an edit box, a list box, or a label on the PropertyManager page

## VBA Syntax

See [PropertyManagerPageControl::BackgroundColor](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~BackgroundColor.html).

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
