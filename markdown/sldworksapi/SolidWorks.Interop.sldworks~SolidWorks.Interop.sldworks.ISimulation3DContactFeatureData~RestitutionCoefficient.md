---
title: "RestitutionCoefficient Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "RestitutionCoefficient"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~RestitutionCoefficient.html"
---

# RestitutionCoefficient Property (ISimulation3DContactFeatureData)

Gets or sets the coefficient of restitution in a 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RestitutionCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim value As System.Double

instance.RestitutionCoefficient = value

value = instance.RestitutionCoefficient
```

### C#

```csharp
System.double RestitutionCoefficient {get; set;}
```

### C++/CLI

```cpp
property System.double RestitutionCoefficient {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Coefficient of restitution

## VBA Syntax

See [Simulation3DContactFeatureData::RestitutionCoefficient](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~RestitutionCoefficient.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## Remarks

Available only when [ISimulation3DContactFeatureData::UseRestitutionCoefficient](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation3DContactFeatureData~UseRestitutionCoefficient.html) is true.

The restitution coefficient is the ratio of relative velocities of two elastic spheres before and after impact.

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
