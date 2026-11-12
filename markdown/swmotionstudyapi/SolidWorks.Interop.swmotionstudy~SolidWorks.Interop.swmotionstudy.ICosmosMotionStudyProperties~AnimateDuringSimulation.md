---
title: "AnimateDuringSimulation Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "AnimateDuringSimulation"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~AnimateDuringSimulation.html"
---

# AnimateDuringSimulation Property (ICosmosMotionStudyProperties)

Gets or sets whether to show the motion during the calculation of the simulation.

## Syntax

### Visual Basic (Declaration)

```vb
Property AnimateDuringSimulation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Boolean

instance.AnimateDuringSimulation = value

value = instance.AnimateDuringSimulation
```

### C#

```csharp
System.bool AnimateDuringSimulation {get; set;}
```

### C++/CLI

```cpp
property System.bool AnimateDuringSimulation {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to show the motion during the calculation of the simulation, false to not and speed up the calculation time

## VBA Syntax

See [CosmosMotionStudyProperties::AnimateDuringSimulation](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~AnimateDuringSimulation.html).

## Examples

[Get Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
