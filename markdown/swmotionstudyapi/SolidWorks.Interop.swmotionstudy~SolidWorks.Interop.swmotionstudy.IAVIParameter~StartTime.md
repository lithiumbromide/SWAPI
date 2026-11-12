---
title: "StartTime Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "StartTime"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~StartTime.html"
---

# StartTime Property (IAVIParameter)

Gets or sets the start time of a specific time period of the animation to save.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Double

instance.StartTime = value

value = instance.StartTime
```

### C#

```csharp
System.double StartTime {get; set;}
```

### C++/CLI

```cpp
property System.double StartTime {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Start time in seconds

## VBA Syntax

See [AVIParameter::StartTime](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~StartTime.html).

## Remarks

By specifying a start time and [end time](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~EndTime.html), you can save a portion of the animation, instead of [saving the entire animation](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~SaveEntireAnimation.html), to the animation file or files.

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
