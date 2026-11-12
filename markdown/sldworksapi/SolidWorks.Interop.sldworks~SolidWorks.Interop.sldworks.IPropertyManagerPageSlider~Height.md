---
title: "Height Property (IPropertyManagerPageSlider)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSlider"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~Height.html"
---

# Height Property (IPropertyManagerPageSlider)

Gets or sets the height of the slider control.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSlider
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

Height of slider control

## VBA Syntax

See [PropertyManagerPageSlider::Height](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSlider~Height.html).

## Examples

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

## Remarks

You can only set this property before the PropertyManager page is displayed.

Normally you should not use this property because SOLIDWORKS will size the slider appropriately based on its orientation and display properties. However, the complexity of the PropertyManager page's layout may make it necessary to use this property with [IPropertyManagerPageControl::Left](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageControl~Left.html), [IPropertyManagerPageControl::Top](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageControl~Top.html), and [IPropertyManagerPageControl::Width](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageControl~Width.html) to get the desired look.

This property is also for creating a small slider by clearing the [IPropertyManagerPageSlider::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~Style.html) swPropMgrPageSliderStyle_AutoTicks bit and setting Height to a value less than the default. A horizontal slider without tick marks has a default height of 16. This height is in dialog-box units. You can convert this value to screen units (pixels) by using the Windows MapDialogRect function.

## See Also

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.html)
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
