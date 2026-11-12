---
title: "CreateFeature Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "CreateFeature"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~CreateFeature.html"
---

# CreateFeature Method (IMotionStudy)

Creates a simulation feature using its feature data object.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeature( _
   ByVal FeatureData As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim FeatureData As System.Object
Dim value As System.Object

value = instance.CreateFeature(FeatureData)
```

### C#

```csharp
System.object CreateFeature(
   System.object FeatureData
)
```

### C++/CLI

```cpp
System.Object^ CreateFeature(
   System.Object^ FeatureData
)
```

### Parameters

- `FeatureData`: Feature data object

### Return Value

[Feature](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [MotionStudy::CreateFeature](ms-its:swmotionstudyapivb6.chm::/swmotionstudy~MotionStudy~CreateFeature.html).

## Examples

[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

## Remarks

You can use [IMotionStudy::CreateDefinition](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~CreateDefinition.html) to populate FeatureData of this method to create these simulation features:

- [3DContact](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation3DContactFeatureData.html)
- [Damper](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationDamperFeatureData.html)
- [Force](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationForceFeatureData.html)ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationDamperFeatureData.html
- [Gravity](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationGravityFeatureData.html)
- [Motor](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationMotorFeatureData.html)
- [Spring](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData.html)

A motion study must be active when defining and creating a simulation feature. If a motion study is not active, then this method returns null or nothing.

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
