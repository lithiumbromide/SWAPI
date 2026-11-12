---
title: "DistanceMotor Method (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "DistanceMotor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DistanceMotor.html"
---

# DistanceMotor Method (ISimulationMotorFeatureData)

Sets the distance and time for which to operate this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DistanceMotor( _
   ByVal Displacement As System.Double, _
   ByVal StartTime As System.Double, _
   ByVal Duration As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim Displacement As System.Double
Dim StartTime As System.Double
Dim Duration As System.Double

instance.DistanceMotor(Displacement, StartTime, Duration)
```

### C#

```csharp
void DistanceMotor(
   System.double Displacement,
   System.double StartTime,
   System.double Duration
)
```

### C++/CLI

```cpp
void DistanceMotor(
   System.double Displacement,
   System.double StartTime,
   System.double Duration
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Displacement`: Displacement in degrees
- `StartTime`: Start time in seconds
- `Duration`: Duration in seconds

## VBA Syntax

See [SimulationMotorFeatureData::DistanceMotor](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~DistanceMotor.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::ConstantSpeedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ConstantSpeedMotor.html)
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.html)
[ISimulationMotorFeatureData::OscillatingMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~OscillatingMotor.html)
[ISimulationMotorFeatureData::Expression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Expression.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
