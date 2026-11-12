---
title: "ScreenHeight Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "ScreenHeight"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~ScreenHeight.html"
---

# ScreenHeight Property (IAVIParameter)

Gets or sets the height at which to display the animation on the screen.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScreenHeight As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Integer

instance.ScreenHeight = value

value = instance.ScreenHeight
```

### C#

```csharp
System.int ScreenHeight {get; set;}
```

### C++/CLI

```cpp
property System.int ScreenHeight {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Height at which to display the animation on the screen

## VBA Syntax

See [AVIParameter::ScreenHeight](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~ScreenHeight.html).

## Remarks

This property is only available when the [image size](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ImageSize.html) is Custom.

To set the width of the image, call [AVIParameter::ScreenWidth](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenWidth.html). To [preserve the aspect ratio](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~PreserveRatio.html) of the animation, specify [screen ratio](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenRatio.html) or a [value](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~AspectRatio.html).

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
