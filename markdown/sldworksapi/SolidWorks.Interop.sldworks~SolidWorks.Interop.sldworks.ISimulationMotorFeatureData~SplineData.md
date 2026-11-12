---
title: "SplineData Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "SplineData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~SplineData.html"
---

# SplineData Property (ISimulationMotorFeatureData)

Gets or sets the spline data points for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SplineData As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.Object

instance.SplineData = value

value = instance.SplineData
```

### C#

```csharp
System.object SplineData {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SplineData {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of spline data points

## VBA Syntax

See [SimulationMotorFeatureData::SplineData](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~SplineData.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::LoadSplineData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadSplineData.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
