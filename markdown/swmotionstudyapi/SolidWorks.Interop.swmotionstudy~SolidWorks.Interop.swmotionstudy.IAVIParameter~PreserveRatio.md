---
title: "PreserveRatio Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "PreserveRatio"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~PreserveRatio.html"
---

# PreserveRatio Property (IAVIParameter)

Gets or sets whether to preserve the aspect ratio of the animation when changing either its [width](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenWidth.html) or [height](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~ScreenHeight.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property PreserveRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Boolean

instance.PreserveRatio = value

value = instance.PreserveRatio
```

### C#

```csharp
System.bool PreserveRatio {get; set;}
```

### C++/CLI

```cpp
property System.bool PreserveRatio {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to preserve the ratio, false to not

## VBA Syntax

See [AVIParameter::PreserveRatio](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~PreserveRatio.html).

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)
[IAVIParameter::AspectRatio Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~AspectRatio.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
