---
title: "CreateDefinition Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "CreateDefinition"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~CreateDefinition.html"
---

# CreateDefinition Method (IMotionStudy)

Creates the definition for the simulation feature data object.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDefinition( _
   ByVal Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim Type As System.Integer
Dim value As System.Object

value = instance.CreateDefinition(Type)
```

### C#

```csharp
System.object CreateDefinition(
   System.int Type
)
```

### C++/CLI

```cpp
System.Object^ CreateDefinition(
   System.int Type
)
```

### Parameters

- `Type`: Type of simulation feature as defined in [swFeatureNameID_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureNameID_e.html):

  - swFmAEMGravity ([ISimulationGravityFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationGravityFeatureData.html))
  - swFmAEMLinearForce ([ISimulationForceFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationForceFeatureData.html))
  - swFmAEMTorque ([ISimulationForceFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationForceFeatureData.html))
  - swFmAEMLinearMotor ([ISimulationMotorFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationMotorFeatureData.html))
  - swFmAEMRotationalMotor ([ISimulationMotorFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationMotorFeatureData.html))
  - swFmAEMLinearDamper ([ISimulationDamperFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationDamperFeatureData.html))
  - swFmAEMTorsionalDamper ([ISimulationDamperFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationDamperFeatureData.html))
  - swFmAEM3DContact ([ISimulation3DContactFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation3DContactFeatureData.html))
  - swFmAEMLinearMotionSpring ([ISimulationSpringFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData.html))
  - swFmAEMTorsionalMotionSpring ([ISimulationSpringFeatureData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData.html))
  - swFmAEMLinearSpring ([ISimulationLinearSpringFeatureData](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData.html))

### Return Value

Feature data object

## VBA Syntax

See [MotionStudy::CreateDefinition](ms-its:swmotionstudyapivb6.chm::/swmotionstudy~MotionStudy~CreateDefinition.html).

## Examples

[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

## Remarks

You can use this method to define a simulation feature data object that is used by [IMotionStudy::CreateFeature](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~CreateFeature.html) to create these simulation features:

- [3DContact](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation3DContactFeatureData.html)
- [Damper](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationDamperFeatureData.html)
- [Force](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationForceFeatureData.html)ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationDamperFeatureData.html
- [Gravity](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationGravityFeatureData.html)
- [Motor](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationMotorFeatureData.html)
- [Spring](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData.html)

A motion study must be active when defining and creating a simulation feature. If a motion study is not active, then this method returns null or Nothing.

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
