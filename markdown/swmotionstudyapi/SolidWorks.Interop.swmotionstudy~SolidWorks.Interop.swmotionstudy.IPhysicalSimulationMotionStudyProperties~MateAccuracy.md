---
title: "MateAccuracy Property (IPhysicalSimulationMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IPhysicalSimulationMotionStudyProperties"
member: "MateAccuracy"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IPhysicalSimulationMotionStudyProperties~MateAccuracy.html"
---

# MateAccuracy Property (IPhysicalSimulationMotionStudyProperties)

Gets or sets the mate accuracy for this Physical Simulation motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Property MateAccuracy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPhysicalSimulationMotionStudyProperties
Dim value As System.Integer

instance.MateAccuracy = value

value = instance.MateAccuracy
```

### C#

```csharp
System.int MateAccuracy {get; set;}
```

### C++/CLI

```cpp
property System.int MateAccuracy {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Mate accuracy

## VBA Syntax

See [PhysicalSimulationMotionStudyProperties::MateAccuracy](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~PhysicalSimulationMotionStudyProperties~MateAccuracy.html).

## Remarks

This property controls the amount of interpenetration of geometric meshes. A lower value for Accuracy allows more mesh interpenetration. This allows for smother motion, especially in tight-fit situations; for example, a ball rolling in a channel with very little clearance.

## See Also

[IPhysicalSimulationMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IPhysicalSimulationMotionStudyProperties.html)
[IPhysicalSimulationMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IPhysicalSimulationMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
