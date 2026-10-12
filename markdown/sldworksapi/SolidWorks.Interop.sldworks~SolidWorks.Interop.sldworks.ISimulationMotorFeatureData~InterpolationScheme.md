---
title: "InterpolationScheme Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "InterpolationScheme"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolationScheme.html"
---

# InterpolationScheme Property (ISimulationMotorFeatureData)

Gets or set the interpolation scheme for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property InterpolationScheme As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.Integer

instance.InterpolationScheme = value

value = instance.InterpolationScheme
```

### C#

```csharp
System.int InterpolationScheme {get; set;}
```

### C++/CLI

```cpp
property System.int InterpolationScheme {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Interpolation scheme

## VBA Syntax

See [SimulationMotorFeatureData::InterpolationScheme](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~InterpolationScheme.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
