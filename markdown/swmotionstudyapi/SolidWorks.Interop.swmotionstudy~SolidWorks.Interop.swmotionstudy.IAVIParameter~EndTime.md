---
title: "EndTime Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "EndTime"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~EndTime.html"
---

# EndTime Property (IAVIParameter)

Gets or sets the end time of a specific time period of the animation to save.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Double

instance.EndTime = value

value = instance.EndTime
```

### C#

```csharp
System.double EndTime {get; set;}
```

### C++/CLI

```cpp
property System.double EndTime {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

End time in seconds

## VBA Syntax

See [AVIParameter::EndTime](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~EndTime.html).

## Remarks

By specifying a [start time](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~StartTime.html) and end time, you can save a portion of the animation, instead of [saving the entire animation](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IAVIParameter~SaveEntireAnimation.html), to the animation file or files.

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
