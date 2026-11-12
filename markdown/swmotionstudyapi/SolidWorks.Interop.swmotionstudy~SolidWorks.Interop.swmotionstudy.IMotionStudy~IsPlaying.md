---
title: "IsPlaying Property (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "IsPlaying"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~IsPlaying.html"
---

# IsPlaying Property (IMotionStudy)

Gets whether this motion study is playing.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsPlaying As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Boolean

value = instance.IsPlaying
```

### C#

```csharp
System.bool IsPlaying {get;}
```

### C++/CLI

```cpp
property System.bool IsPlaying {
   System.bool get();
}
```

### Property Value

True if this motion study is playing, false if not

## VBA Syntax

See [MotionStudy::IsPlaying](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~IsPlaying.html).

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::Play Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Play.html)
[IMotionStudy::PlayFromStart Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayFromStart.html)
[IMotionStudy::PlayMode Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayMode.html)
[IMotionStudy::Stop Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Stop.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
