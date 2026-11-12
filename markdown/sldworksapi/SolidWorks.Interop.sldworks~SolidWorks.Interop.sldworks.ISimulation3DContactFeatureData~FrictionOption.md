---
title: "FrictionOption Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "FrictionOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~FrictionOption.html"
---

# FrictionOption Property (ISimulation3DContactFeatureData)

Gets or sets whether contact friction is off, full (static), or dynamic in a 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrictionOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim value As System.Integer

instance.FrictionOption = value

value = instance.FrictionOption
```

### C#

```csharp
System.int FrictionOption {get; set;}
```

### C++/CLI

```cpp
property System.int FrictionOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Friction as defined in [swMotionContactFrictionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMotionContactFrictionType_e.html)

## VBA Syntax

See [Simulation3DContactFeatureData::FrictionOption](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~FrictionOption.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)
[ISimulation3DContactFeatureData::DynamicFrictionCoefficient Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~DynamicFrictionCoefficient.html)
[ISimulation3DContactFeatureData::DynamicFrictionVelocity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~DynamicFrictionVelocity.html)
[ISimulation3DContactFeatureData::StaticFrictionCoefficient Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~StaticFrictionCoefficient.html)
[ISimulation3DContactFeatureData::StaticFrictionVelocity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~StaticFrictionVelocity.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
