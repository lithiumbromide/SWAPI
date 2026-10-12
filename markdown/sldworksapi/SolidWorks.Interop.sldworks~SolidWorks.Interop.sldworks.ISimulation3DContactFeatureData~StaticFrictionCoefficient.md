---
title: "StaticFrictionCoefficient Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "StaticFrictionCoefficient"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~StaticFrictionCoefficient.html"
---

# StaticFrictionCoefficient Property (ISimulation3DContactFeatureData)

Gets or sets the static friction coefficent in a 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property StaticFrictionCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim value As System.Double

instance.StaticFrictionCoefficient = value

value = instance.StaticFrictionCoefficient
```

### C#

```csharp
System.double StaticFrictionCoefficient {get; set;}
```

### C++/CLI

```cpp
property System.double StaticFrictionCoefficient {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Static friction coefficient

## VBA Syntax

See [Simulation3DContactFeatureData::StaticFrictionCoefficient](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~StaticFrictionCoefficient.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## Remarks

Available only when [ISimulation3DContactFeatureData::FrictionOption](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation3DContactFeatureData~FrictionOption.html) is [swMotionContactFrictionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMotionContactFrictionType_e.html).swMotionContactFrictionFull.

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)
[ISimulation3DContactFeatureData::StaticFrictionVelocity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~StaticFrictionVelocity.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
