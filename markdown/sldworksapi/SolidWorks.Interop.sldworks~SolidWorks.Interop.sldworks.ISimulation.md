---
title: "ISimulation Interface"
project: "SOLIDWORKS API Help"
interface: "ISimulation"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.html"
---

# ISimulation Interface

This interface is:

- obsolete and has not been superseded.
- nonfunctional in SOLIDWORKS 2008 and later.

Use the interfaces related to [motion studies](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyManager.html) introduced in SOLIDWORKS 2008 to access animation and simulation.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISimulation
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation
```

### C#

```csharp
public interface ISimulation
```

### C++/CLI

```cpp
public interface class ISimulation
```

## VBA Syntax

See [Simulation](ms-its:sldworksapivb6.chm::/sldworks~Simulation.html).

## Remarks

Do not confuse Physical Simulation with [animation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnimation.html). The SOLIDWORKS Design software computes a Physical Simulation, which generates a number of steps (and transforms) and elapsed time for those steps. The SOLIDWORKS Design software then displays the computed Physical Simulation using animation. To create the display, the animation process takes the Physical Simulation steps and does a linear interpolation of those steps for the elapsed time. The elapsed time and frames of Physical Simulation will most likely be different than the elapsed time and frames of an animation.

## See Also

[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
