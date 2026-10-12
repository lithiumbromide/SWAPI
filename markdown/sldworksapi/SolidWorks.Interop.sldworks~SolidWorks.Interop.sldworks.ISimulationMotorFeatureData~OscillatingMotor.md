---
title: "OscillatingMotor Method (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "OscillatingMotor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~OscillatingMotor.html"
---

# OscillatingMotor Method (ISimulationMotorFeatureData)

Sets the displacement and frequency for oscillating motion for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OscillatingMotor( _
   ByVal Displacement As System.Double, _
   ByVal Frequency As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim Displacement As System.Double
Dim Frequency As System.Double

instance.OscillatingMotor(Displacement, Frequency)
```

### C#

```csharp
void OscillatingMotor(
   System.double Displacement,
   System.double Frequency
)
```

### C++/CLI

```cpp
void OscillatingMotor(
   System.double Displacement,
   System.double Frequency
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Displacement`: Displacement in degrees
- `Frequency`: Frequency in Hz

## VBA Syntax

See [SimulationMotorFeatureData::OscillatingMotor](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~OscillatingMotor.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::ConstantSpeedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ConstantSpeedMotor.html)
[ISimulationMotorFeatureData::DistanceMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DistanceMotor.html)
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.html)
[ISimulationMotorFeatureData::Expression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Expression.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
