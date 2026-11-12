---
title: "ConstantSpeedMotor Method (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "ConstantSpeedMotor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ConstantSpeedMotor.html"
---

# ConstantSpeedMotor Method (ISimulationMotorFeatureData)

Sets the constant speed for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ConstantSpeedMotor( _
   ByVal Speed As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim Speed As System.Double

instance.ConstantSpeedMotor(Speed)
```

### C#

```csharp
void ConstantSpeedMotor(
   System.double Speed
)
```

### C++/CLI

```cpp
void ConstantSpeedMotor(
   System.double Speed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Speed`: Constant speed in RPMs

## VBA Syntax

See [SimulationMotorFeatureData::ConstantSpeedMotor](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~ConstantSpeedMotor.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::DistanceMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DistanceMotor.html)
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.html)
[ISimulationMotorFeatureData::OscillatingMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~OscillatingMotor.html)
[ISimulationMotorFeatureData::Expression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Expression.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
