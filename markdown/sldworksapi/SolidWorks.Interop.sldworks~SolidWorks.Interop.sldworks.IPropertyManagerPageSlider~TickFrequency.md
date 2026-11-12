---
title: "TickFrequency Property (IPropertyManagerPageSlider)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSlider"
member: "TickFrequency"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~TickFrequency.html"
---

# TickFrequency Property (IPropertyManagerPageSlider)

Gets or sets the frequency of tick marks on a slider.

## Syntax

### Visual Basic (Declaration)

```vb
Property TickFrequency As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSlider
Dim value As System.Integer

instance.TickFrequency = value

value = instance.TickFrequency
```

### C#

```csharp
System.int TickFrequency {get; set;}
```

### C++/CLI

```cpp
property System.int TickFrequency {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Frequency of tick marks on slider

## VBA Syntax

See [PropertyManagerPageSlider::TickFrequency](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSlider~TickFrequency.html).

## Remarks

If you set the frequency to 1, then a tick mark appears on every increment in the [range](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~SetRange.html). A value of 10 means that a tick mark appears every 10 increments in the range. If you do not set a frequency, then the frequency of tick marks default to 1.

[IPropertyManagerPageSlider::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~Style.html) must be set to swPropMgrPageSliderStyle_AutoTicks to set IPropertyManagerPageSlider::TickFrequency.

## See Also

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.html)
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
