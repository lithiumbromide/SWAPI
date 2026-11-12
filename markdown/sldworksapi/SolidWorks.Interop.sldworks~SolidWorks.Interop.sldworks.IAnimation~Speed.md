---
title: "Speed Property (IAnimation)"
project: "SOLIDWORKS API Help"
interface: "IAnimation"
member: "Speed"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~Speed.html"
---

# Speed Property (IAnimation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Property Speed As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnimation
Dim value As System.Integer

instance.Speed = value

value = instance.Speed
```

### C#

```csharp
System.int Speed {get; set;}
```

### C++/CLI

```cpp
property System.int Speed {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Speed at which the animation plays as defined by [swAnimationPlaySpeed_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnimationPlaySpeed_e.html)

## VBA Syntax

See [Animation::Speed](ms-its:sldworksapivb6.chm::/sldworks~Animation~Speed.html).

## Remarks

This property affects the duration of the animation. It allows you to specify whether
or not to play the animation at half speed or double speed, which halves or doubles
the animation duration.

If you use [IAnimation::Duration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnimation~Speed.html) while an animation is playing, then you might not get
the same result as when the animation is not running.

| If you get the Animation object using... | And then use... | Then the duration... |
| --- | --- | --- |
| ISimulation::Animation | Animation::Duration | Is at the normal playing speed |
| ISimulation::PlayAnimation | Animation::Duration | Might be a different value because the animation is playing and the Animation Controller speed may be set to Normal , Slow Play , or Fast Play |

## See Also

[IAnimation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.html)
[IAnimation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
