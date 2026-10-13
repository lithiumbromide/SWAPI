---
title: "PlayAnimation Method (ISimulation)"
project: "SOLIDWORKS API Help"
interface: "ISimulation"
member: "PlayAnimation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~PlayAnimation.html"
---

# PlayAnimation Method (ISimulation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function PlayAnimation() As Animation
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation
Dim value As Animation

value = instance.PlayAnimation()
```

### C#

```csharp
Animation PlayAnimation()
```

### C++/CLI

```cpp
Animation^ PlayAnimation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Animation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnimation.html)

## VBA Syntax

See [Simulation::PlayAnimation](ms-its:sldworksapivb6.chm::/sldworks~Simulation~PlayAnimation.html).

## Remarks

If an animation is playing when this method is used, then this method returns the [IAnimation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnimation.html) object for that animation. To check to see if an animation is currently playing, use [ISimulation::IsAnimationPlaying](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation~IsAnimationPlaying.html).

## See Also

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.html)
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
