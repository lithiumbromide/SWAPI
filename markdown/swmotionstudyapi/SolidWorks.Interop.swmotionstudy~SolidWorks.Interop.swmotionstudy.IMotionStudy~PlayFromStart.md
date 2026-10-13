---
title: "PlayFromStart Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "PlayFromStart"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayFromStart.html"
---

# PlayFromStart Method (IMotionStudy)

Plays this motion study from the beginning.

## Syntax

### Visual Basic (Declaration)

```vb
Function PlayFromStart() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Boolean

value = instance.PlayFromStart()
```

### C#

```csharp
System.bool PlayFromStart()
```

### C++/CLI

```cpp
System.bool PlayFromStart();
```

### Return Value

True if the motion study plays from where the animation timebar is located, false if not

## VBA Syntax

See [MotionStudy::PlayFromStart](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~PlayFromStart.html).

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::Play Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Play.html)
[IMotionStudy::IsPlaying Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~IsPlaying.html)
[IMotionStudy::PlayMode Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayMode.html)
[IMotionStudy::Stop Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Stop.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
