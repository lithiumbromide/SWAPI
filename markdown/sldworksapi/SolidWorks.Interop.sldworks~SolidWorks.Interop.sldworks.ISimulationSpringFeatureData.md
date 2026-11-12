---
title: "ISimulationSpringFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html"
---

# ISimulationSpringFeatureData Interface

Allows access to the data that defines a simulation spring feature in SOLIDWORKS Motion studies.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISimulationSpringFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
```

### C#

```csharp
public interface ISimulationSpringFeatureData
```

### C++/CLI

```cpp
public interface class ISimulationSpringFeatureData
```

## VBA Syntax

See [SimulationSpringFeatureData](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData.html).

## Examples

[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

## Remarks

Motion due to motors supersedes motion due to springs. If you have a motor moving a component to the left and a spring pulling a component to the right, the component moves to the left, and the power consumption of the motor increases.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

[IMotionStudy::CreateFeature](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~CreateFeature.html)

## Access Diagram

[SimulationSpringFeatureData](SWObjectModel.pdf#SimulationSpringFeatureData)

## See Also

[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.html)
[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html)
[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
