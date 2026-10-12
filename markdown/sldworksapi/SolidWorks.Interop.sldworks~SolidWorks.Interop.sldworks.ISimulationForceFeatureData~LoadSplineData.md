---
title: "LoadSplineData Method (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "LoadSplineData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~LoadSplineData.html"
---

# LoadSplineData Method (ISimulationForceFeatureData)

Loads the spline data from the specified file for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadSplineData( _
   ByVal Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
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

## VBA Syntax

See [SimulationForceFeatureData::LoadSplineData](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~LoadSplineData.html).

## Remarks

The file should contain one data point per line. The data point consists of two values:

- Time
- Value at that time

Use commas or spaces as separators between the values.

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
