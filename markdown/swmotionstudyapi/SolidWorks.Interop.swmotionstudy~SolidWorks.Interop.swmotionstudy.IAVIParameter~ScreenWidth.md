---
title: "ScreenWidth Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "ScreenWidth"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~ScreenWidth.html"
---

# ScreenWidth Property (IAVIParameter)

Gets or sets the width at which to display the animation on the screen.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScreenWidth As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Integer

instance.ScreenWidth = value

value = instance.ScreenWidth
```

### C#

```csharp
System.int ScreenWidth {get; set;}
```

### C++/CLI

```cpp
property System.int ScreenWidth {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Width at which to display the animation on the screen

## VBA Syntax

See [AVIParameter::ScreenWidth](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~ScreenWidth.html).

## Remarks

This property is only available when the [image size](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ImageSize.html) is Custom.

To set the height of the image, call [AVIParameter::ScreenHeight](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenHeight.html). To [preserve the aspect ratio](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~PreserveRatio.html) of the animation, specify [screen ratio](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenRatio.html) or a [value](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~AspectRatio.html).

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
