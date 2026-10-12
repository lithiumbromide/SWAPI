---
title: "FunctionInterpolatedValues Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "FunctionInterpolatedValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionInterpolatedValues.html"
---

# FunctionInterpolatedValues Property (ISimulationForceFeatureData)

Gets or sets the interpolated values for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FunctionInterpolatedValues As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.Object

instance.FunctionInterpolatedValues = value

value = instance.FunctionInterpolatedValues
```

### C#

```csharp
System.object FunctionInterpolatedValues {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FunctionInterpolatedValues {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of interpolated values (time and force)

## VBA Syntax

See [SimulationForceFeatureData::FunctionInterpolatedValues](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~FunctionInterpolatedValues.html).

## Remarks

SOLIDWORKS interpolates a spline betweeen the data points.

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::GetInterpolatedValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetInterpolatedValue.html)
[ISimulationForceFeatureData::InterpolationScheme Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~InterpolationScheme.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
