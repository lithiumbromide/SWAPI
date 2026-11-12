---
title: "Left Property (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "Left"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Left.html"
---

# Left Property (IPropertyManagerPageControl)

Gets or sets the left edge of the control on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property Left As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim value As System.Short

instance.Left = value

value = instance.Left
```

### C#

```csharp
System.short Left {get; set;}
```

### C++/CLI

```cpp
property System.short Left {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Left edge of the control

## VBA Syntax

See [PropertyManagerPageControl::Left](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~Left.html).

## Remarks

This property must be set before the control is displayed.

If you do not specify the position and size of the controls on the PropertyManager page, the controls are created using a default size and placed in a computed default position so that your page matches the look-and-feel of a SOLIDWORKS PropertyManager page. This is generally the best way to go, whenever possible. However, while there are no limitations on how you create the layout of your page, it is recommended that you only use this method if you want to place controls on the page.

By default, the left edge of a control is either the left edge of its group box or indented a certain distance. This is determined by the LeftAlign argument of the [IPropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) or [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html) method. Using IPropertyManagerPage2::AddControl or IPropertyManagerPage2::IAddControl overrides that default. The value is in dialog units relative to the group box that the control is in. The left edge of the group box is 0; the right edge of the group box is 100.

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
