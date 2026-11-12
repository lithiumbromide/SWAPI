---
title: "GetInterpolatedValue Method (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "GetInterpolatedValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetInterpolatedValue.html"
---

# GetInterpolatedValue Method (ISimulationForceFeatureData)

Gets the interpolated value at the specified time for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInterpolatedValue( _
   ByVal Time As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
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

- `Time`: Time at which to get the interpolated value

### Return Value

Interpolated value

## VBA Syntax

See [SimulationForceFeatureData::GetInterpolatedValue](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~GetInterpolatedValue.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::InterpolationScheme Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~InterpolationScheme.html)
[ISimulationForceFeatureData::FunctionInterpolatedValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionInterpolatedValues.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
