---
title: "Stop Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "Stop"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Stop.html"
---

# Stop Method (IMotionStudy)

Stops the currently playing animation.

## Syntax

### Visual Basic (Declaration)

```vb
Function Stop() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Boolean

value = instance.Stop()
```

### C#

```csharp
System.bool Stop()
```

### C++/CLI

```cpp
System.bool Stop();
```

### Return Value

True if the currently playing stops playing, false if not

## VBA Syntax

See [MotionStudy::Stop](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~Stop.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::Play Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Play.html)
[IMotionStudy::PlayFromStart Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayFromStart.html)
[IMotionStudy::IsPlaying Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~IsPlaying.html)
[IMotionStudy::PlayMode Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayMode.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
