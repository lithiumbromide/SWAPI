---
title: "Height Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Height.html"
---

# Height Property (IPropertyManagerPageSelectionbox)

Gets or sets the height of this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
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

Selection box height

## VBA Syntax

See [PropertyManagerPageSelectionbox::Height](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~Height.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

The height is in dialog-box units. You can convert these values to screen units (pixels) by using the MapDialogRect function.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
