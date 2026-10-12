---
title: "SetFrameRate Method (IMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyProperties"
member: "SetFrameRate"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyProperties~SetFrameRate.html"
---

# SetFrameRate Method (IMotionStudyProperties)

Sets the number of frames per second for this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFrameRate( _
   ByVal FramesPerSecond As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudyProperties
Dim FramesPerSecond As System.Integer
Dim value As System.Boolean

value = instance.SetFrameRate(FramesPerSecond)
```

### C#

```csharp
System.bool SetFrameRate(
   System.int FramesPerSecond
)
```

### C++/CLI

```cpp
System.bool SetFrameRate(
   System.int FramesPerSecond
)
```

### Parameters

- `FramesPerSecond`: Number of frames per second

### Return Value

True if the frame rate is set, false if not

## VBA Syntax

See [MotionStudyProperties::SetFrameRate](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyProperties~SetFrameRate.html).

## See Also

[IMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyProperties.html)
[IMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyProperties_members.html)
[IMotionStudyProperties::GetFrameRate Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyProperties~GetFrameRate.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
