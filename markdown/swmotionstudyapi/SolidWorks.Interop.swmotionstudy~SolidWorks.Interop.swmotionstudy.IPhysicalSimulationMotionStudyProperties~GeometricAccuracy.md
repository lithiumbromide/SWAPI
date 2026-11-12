---
title: "GeometricAccuracy Property (IPhysicalSimulationMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IPhysicalSimulationMotionStudyProperties"
member: "GeometricAccuracy"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IPhysicalSimulationMotionStudyProperties~GeometricAccuracy.html"
---

# GeometricAccuracy Property (IPhysicalSimulationMotionStudyProperties)

Gets or sets the geometric accuracy of this Physical Simulation motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Property GeometricAccuracy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPhysicalSimulationMotionStudyProperties
Dim value As System.Integer

instance.GeometricAccuracy = value

value = instance.GeometricAccuracy
```

### C#

```csharp
System.int GeometricAccuracy {get; set;}
```

### C++/CLI

```cpp
property System.int GeometricAccuracy {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Geometric accuracy

## VBA Syntax

See [PhysicalSimulationMotionStudyProperties::GeometricAccuracy](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~PhysicalSimulationMotionStudyProperties~GeometricAccuracy.html).

## Remarks

Physical Simulation creates meshes from curved geometry. The higher the value for Accuracy, the closer to actual geometry the mesh becomes. This makes collision simulation more accurate, but requires more time to compute.

## See Also

[IPhysicalSimulationMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IPhysicalSimulationMotionStudyProperties.html)
[IPhysicalSimulationMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IPhysicalSimulationMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
