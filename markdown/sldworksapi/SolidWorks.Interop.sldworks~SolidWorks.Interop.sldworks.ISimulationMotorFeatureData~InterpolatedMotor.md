---
title: "InterpolatedMotor Method (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "InterpolatedMotor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.html"
---

# InterpolatedMotor Method (ISimulationMotorFeatureData)

Sets the drive type and interpolation scheme for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InterpolatedMotor( _
   ByVal DriveType As System.Integer, _
   ByVal InterpolationScheme As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim DriveType As System.Integer
Dim InterpolationScheme As System.Integer

instance.InterpolatedMotor(DriveType, InterpolationScheme)
```

### C#

```csharp
void InterpolatedMotor(
   System.int DriveType,
   System.int InterpolationScheme
)
```

### C++/CLI

```cpp
void InterpolatedMotor(
   System.int DriveType,
   System.int InterpolationScheme
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DriveType`: Drive type as defined in [swSimulationMotorDriveType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationMotorDriveType_e.html)
- `InterpolationScheme`: Interpolation scheme

## VBA Syntax

See [SimulationMotorFeatureData::InterpolatedMotor](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~InterpolatedMotor.html).

## Examples

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::GetInterpolatedValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~GetInterpolatedValue.html)
[ISimulationMotorFeatureData::InterpolationScheme Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolationScheme.html)
[ISimulationMotorFeatureData::ConstantSpeedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ConstantSpeedMotor.html)
[ISimulationMotorFeatureData::DistanceMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DistanceMotor.html)
[ISimulationMotorFeatureData::OscillatingMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~OscillatingMotor.html)
[ISimulationMotorFeatureData::Expression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Expression.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
