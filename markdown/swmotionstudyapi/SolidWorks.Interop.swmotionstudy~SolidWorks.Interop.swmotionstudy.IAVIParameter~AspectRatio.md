---
title: "AspectRatio Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "AspectRatio"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~AspectRatio.html"
---

# AspectRatio Property (IAVIParameter)

Gets or sets the ratio between the [width](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenWidth.html) of the image and the [height](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenHeight.html) of the image for the animation.

## Syntax

### Visual Basic (Declaration)

```vb
Property AspectRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Double

instance.AspectRatio = value

value = instance.AspectRatio
```

### C#

```csharp
System.double AspectRatio {get; set;}
```

### C++/CLI

```cpp
property System.double AspectRatio {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Aspect ratio

## VBA Syntax

See [AVIParameter::AspectRatio](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~AspectRatio.html).

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)
[IAVIParamter::PreserveRatio Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~PreserveRatio.html)
[IAVIParameter::ScreenRatio Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~ScreenRatio.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
