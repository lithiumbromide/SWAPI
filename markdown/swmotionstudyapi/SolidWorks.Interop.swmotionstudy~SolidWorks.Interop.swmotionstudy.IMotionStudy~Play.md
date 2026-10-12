---
title: "Play Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "Play"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Play.html"
---

# Play Method (IMotionStudy)

Plays the animation; the start point is where the animation timebar is located.

## Syntax

### Visual Basic (Declaration)

```vb
Function Play() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Boolean

value = instance.Play()
```

### C#

```csharp
System.bool Play()
```

### C++/CLI

```cpp
System.bool Play();
```

### Return Value

True if the motion study plays from where the animation timebar is located, false if not

## VBA Syntax

See [MotionStudy::Play](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~Play.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::IsPlaying Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~IsPlaying.html)
[IMotionStudy::PlayMode Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayMode.html)
[IMotionStudy::PlayFromStart Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayFromStart.html)
[IMotionStudy::Stop Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Stop.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
