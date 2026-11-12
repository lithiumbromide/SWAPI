---
title: "SetTime Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "SetTime"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SetTime.html"
---

# SetTime Method (IMotionStudy)

Sets the time, in seconds, where to place the timebar on the timeline for this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTime( _
   ByVal Time As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim Time As System.Double
Dim value As System.Boolean

value = instance.SetTime(Time)
```

### C#

```csharp
System.bool SetTime(
   System.double Time
)
```

### C++/CLI

```cpp
System.bool SetTime(
   System.double Time
)
```

### Parameters

- `Time`: Time, in seconds, where to place the timebar on the timeline

### Return Value

True if the timebar is set to the specified time, false if not

## VBA Syntax

See [MotionStudy::SetTime](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~SetTime.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::GetTime Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetTime.html)
[IMotionStudy::GetDuration Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetDuration.html)
[IMotionStudy::SetDuration Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SetDuration.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
