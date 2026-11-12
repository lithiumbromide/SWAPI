---
title: "DynamicFrictionCoefficient Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "DynamicFrictionCoefficient"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~DynamicFrictionCoefficient.html"
---

# DynamicFrictionCoefficient Property (ISimulation3DContactFeatureData)

Gets or sets the dynamic friction coefficient in a 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DynamicFrictionCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim value As System.Double

instance.DynamicFrictionCoefficient = value

value = instance.DynamicFrictionCoefficient
```

### C#

```csharp
System.double DynamicFrictionCoefficient {get; set;}
```

### C++/CLI

```cpp
property System.double DynamicFrictionCoefficient {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Dynamic friction coefficient

## VBA Syntax

See [Simulation3DContactFeatureData::DynamicFrictionCoefficient](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~DynamicFrictionCoefficient.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## Remarks

Available only when [ISimulation3DContactFeatureData::FrictionOption](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation3DContactFeatureData~FrictionOption.html) is [swMotionContactFrictionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMotionContactFrictionType_e.html).swMotionContactFrictionDynamic.

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)
[ISimulation3DContactFeatureData::DynamicFrictionVelocity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~DynamicFrictionVelocity.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
