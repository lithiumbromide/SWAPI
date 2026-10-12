---
title: "InterpolationScheme Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "InterpolationScheme"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~InterpolationScheme.html"
---

# InterpolationScheme Property (ISimulationForceFeatureData)

Gets the interopolation scheme for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property InterpolationScheme As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
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

Interpolation scheme as defined by [swInterpolationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInterpolationType_e.html)

## VBA Syntax

See [SimulationForceFeatureData::InterpolationScheme](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~InterpolationScheme.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::GetInterpolatedValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetInterpolatedValue.html)
[ISimulationForceFeatureData::FunctionInterpolatedValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionInterpolatedValues.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
