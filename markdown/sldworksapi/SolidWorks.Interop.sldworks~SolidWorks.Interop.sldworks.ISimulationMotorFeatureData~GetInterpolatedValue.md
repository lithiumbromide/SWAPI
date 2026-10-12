---
title: "GetInterpolatedValue Method (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "GetInterpolatedValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~GetInterpolatedValue.html"
---

# GetInterpolatedValue Method (ISimulationMotorFeatureData)

Gets the interopolated value at the specified time for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInterpolatedValue( _
   ByVal Time As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim Time As System.Double
Dim value As System.Double

value = instance.GetInterpolatedValue(Time)
```

### C#

```csharp
System.double GetInterpolatedValue(
   System.double Time
)
```

### C++/CLI

```cpp
System.double GetInterpolatedValue(
   System.double Time
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Time`: Time for which you want the interpolated value

### Return Value

Interpolated value at the specfied time

## VBA Syntax

See [SimulationMotorFeatureData::GetInterpolatedValue](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~GetInterpolatedValue.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.html)
[ISimulationMotorFeatureData::InterpolationScheme Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolationScheme.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
