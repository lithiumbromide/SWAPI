---
title: "Height Property (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~Height.html"
---

# Height Property (IPropertyManagerPageListbox)

Gets and sets the height of the attached drop-down list for this list box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
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

Height (see **Remarks**)

## VBA Syntax

See [PropertyManagerPageListbox::Height](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageListbox~Height.html).

## Examples

See the [IPropertyManagerPageListbox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html) examples.

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

| Value | Result |
| --- | --- |
| 0 | Default height with no scrolling |
| 1 < 30 | Specified height and no scrolling |
| >30 | Specified height and scrolling, but no auto sizing |

The height is in dialog-box units. You can convert these values to screen units (pixels) by using the Windows MapDialogRect function.

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
