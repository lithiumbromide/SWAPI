---
title: "ScreenRatio Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "ScreenRatio"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~ScreenRatio.html"
---

# ScreenRatio Property (IAVIParameter)

Gets or sets whether to base the aspect ratio on the screen.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScreenRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Boolean

instance.ScreenRatio = value

value = instance.ScreenRatio
```

### C#

```csharp
System.bool ScreenRatio {get; set;}
```

### C++/CLI

```cpp
property System.bool ScreenRatio {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to base the aspect ratio on the screen, false to not

## VBA Syntax

See [AVIParameter::ScreenRatio](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~ScreenRatio.html).

## Remarks

This property is only available when the [image size](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ImageSize.html) is Custom and [preserve aspect ratio](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~PreserveRatio.html) is selected.

You can also base the aspect ratio on a [value](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~AspectRatio.html).

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
