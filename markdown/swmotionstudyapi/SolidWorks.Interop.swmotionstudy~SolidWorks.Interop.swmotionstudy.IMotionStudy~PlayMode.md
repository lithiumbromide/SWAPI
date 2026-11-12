---
title: "PlayMode Property (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "PlayMode"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayMode.html"
---

# PlayMode Property (IMotionStudy)

Gets the mode in which this motion study is playing or sets the mode in which to play this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlayMode As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Integer

instance.PlayMode = value

value = instance.PlayMode
```

### C#

```csharp
System.int PlayMode {get; set;}
```

### C++/CLI

```cpp
property System.int PlayMode {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Mode in which this motion study is playing or mode in which to play this motion study as defined in [swAnimationPlayMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnimationPlayMode_e.html)

## VBA Syntax

See [MotionStudy::PlayMode](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~PlayMode.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::IsPlaying Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~IsPlaying.html)
[IMotionStudy::PlayFromStart Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~PlayFromStart.html)
[IMotionStudy::Play Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Play.html)
[IMotionStudy::Stop Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Stop.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
