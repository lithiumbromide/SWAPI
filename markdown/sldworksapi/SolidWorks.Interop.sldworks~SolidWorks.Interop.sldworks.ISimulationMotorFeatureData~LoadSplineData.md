---
title: "LoadSplineData Method (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "LoadSplineData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadSplineData.html"
---

# LoadSplineData Method (ISimulationMotorFeatureData)

Loads the spline data from the specified file for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadSplineData( _
   ByVal Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim Value As System.String
Dim value As System.Boolean

value = instance.LoadSplineData(Value)
```

### C#

```csharp
System.bool LoadSplineData(
   System.string Value
)
```

### C++/CLI

```cpp
System.bool LoadSplineData(
   System.String^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: File from which to load the spline data point values

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [SimulationMotorFeatureData::LoadSplineData](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~LoadSplineData.html).

## Examples

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

## Remarks

The file should contain one data point per line. The data point consists of two values:

- Time
- Value at that time

Use commas or spaces as separators between the values.

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::SplineData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~SplineData.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
