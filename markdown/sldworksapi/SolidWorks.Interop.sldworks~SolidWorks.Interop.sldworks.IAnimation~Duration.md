---
title: "Duration Property (IAnimation)"
project: "SOLIDWORKS API Help"
interface: "IAnimation"
member: "Duration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~Duration.html"
---

# Duration Property (IAnimation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Duration As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAnimation
Dim value As System.Double

value = instance.Duration
```

### C#

```csharp
System.double Duration {get;}
```

### C++/CLI

```cpp
property System.double Duration {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of time, in seconds, this animation plays

## VBA Syntax

See [Animation::Duration](ms-its:sldworksapivb6.chm::/sldworks~Animation~Duration.html).

## Remarks

[IAnimation::Speed](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnimation~Speed.html) affects the duration of the animation. Animation::Speed allows you
to specify whether or not to play the animation at half speed or double speed, which
halves or doubles the animation duration.

If you use Animation::Duration while an animation is playing, then you might not get
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
