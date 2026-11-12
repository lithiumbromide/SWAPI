---
title: "Animation Property (ISimulation)"
project: "SOLIDWORKS API Help"
interface: "ISimulation"
member: "Animation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~Animation.html"
---

# Animation Property (ISimulation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Animation As Animation
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation
Dim value As Animation

value = instance.Animation
```

### C#

```csharp
Animation Animation {get;}
```

### C++/CLI

```cpp
property Animation^ Animation {
   Animation^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Animation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnimation.html)

## VBA Syntax

See [Simulation::Animation](ms-its:sldworksapivb6.chm::/sldworks~Simulation~Animation.html).

## Remarks

| To... | Then.. . |
| --- | --- |
| Get the duration of an animation | Use IAnimation::Duration after using this property |
| Play the animation | Use IAnimation::Play after using this property |
| Display the Animation Controller pop-up toolbar | Use ISimulation::PlayAnimation instead of using this property |

NOTE: Use only the following IAnimation property and method with ISimulation::Animation: IAnimation::Duration and IAnimation::PlayAnimation. The other IAnimation properties and methods do nothing with an IAnimation object returned by ISimlulation::Animation because they expect an animation to be playing. Use [ISimluation::IsAnimationPlaying](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation~IsAnimationPlaying.html) to determine whether an animation is playing.

## See Also

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.html)
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
