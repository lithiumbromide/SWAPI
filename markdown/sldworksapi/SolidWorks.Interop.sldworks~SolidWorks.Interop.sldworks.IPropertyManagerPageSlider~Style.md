---
title: "Style Property (IPropertyManagerPageSlider)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSlider"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~Style.html"
---

# Style Property (IPropertyManagerPageSlider)

Gets or sets the display properties of a slider control.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSlider
Dim value As System.Integer

instance.Style = value

value = instance.Style
```

### C#

```csharp
System.int Style {get; set;}
```

### C++/CLI

```cpp
property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Display properties of slider control as defined in [swPropMgrPageSliderStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageSliderStyle_e.html)

## VBA Syntax

See [PropertyManagerPageSlider::Style](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSlider~Style.html).

## Examples

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

## Remarks

If you do not set the any display properties, then the value is set to 0, which means:

- Slider is horizontal.
- Slider has not ticks.
- Your application is only notified when the user is done dragging the slider to move it.

## See Also

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.html)
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
