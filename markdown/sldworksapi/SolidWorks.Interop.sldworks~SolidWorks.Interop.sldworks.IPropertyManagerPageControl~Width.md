---
title: "Width Property (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "Width"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Width.html"
---

# Width Property (IPropertyManagerPageControl)

Gets or sets the width of the control on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim value As System.Short

instance.Width = value

value = instance.Width
```

### C#

```csharp
System.short Width {get; set;}
```

### C++/CLI

```cpp
property System.short Width {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Width of the control

## VBA Syntax

See [PropertyManagerPageControl::Width](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~Width.html).

## Remarks

This property must be set before the control is displayed.

If you do not specify the position and size of the controls on the PropertyManager page, the controls are created using a default size and placed in a computed default position so that your page matches the look-and-feel of a SOLIDWORKS page. This is generally the best way to go, whenever possible. However, while there are no limitations on how you create the layout of your page, it is recommended that you only use this API if you want to explicitly place controls on the page.

By default, the width of the control is usually set so that it extends to the right edge of its group box. Using this API overrides that default. The value is in dialog units relative to the group box that the control is in. The width of the group box is 100.

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
