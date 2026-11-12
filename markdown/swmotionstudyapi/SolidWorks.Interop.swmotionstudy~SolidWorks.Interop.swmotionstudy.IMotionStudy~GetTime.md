---
title: "GetTime Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "GetTime"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetTime.html"
---

# GetTime Method (IMotionStudy)

Gets the time, in seconds, where the timebar is on the timeline for this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTime() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Double

value = instance.GetTime()
```

### C#

```csharp
System.double GetTime()
```

### C++/CLI

```cpp
System.double GetTime();
```

### Return Value

Time, in seconds, where the timebar is on the timeline

## VBA Syntax

See [MotionStudy::GetTime](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~GetTime.html).

## Examples

[Get Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::GetDuration Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetDuration.html)
[IMotionStudy::SetDuration Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SetDuration.html)
[IMotionStudy::SetTime Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SetTime.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
