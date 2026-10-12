---
title: "UseRestitutionCoefficient Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "UseRestitutionCoefficient"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~UseRestitutionCoefficient.html"
---

# UseRestitutionCoefficient Property (ISimulation3DContactFeatureData)

Gets or sets whether to use the restitution coefficient instead of impact force in a 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseRestitutionCoefficient As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim value As System.Boolean

instance.UseRestitutionCoefficient = value

value = instance.UseRestitutionCoefficient
```

### C#

```csharp
System.bool UseRestitutionCoefficient {get; set;}
```

### C++/CLI

```cpp
property System.bool UseRestitutionCoefficient {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the restitution coefficient, false to use impact force

## VBA Syntax

See [Simulation3DContactFeatureData::UseRestitutionCoefficient](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~UseRestitutionCoefficient.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)
[ISimulation3DContactFeatureData::MaxDamping Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~MaxDamping.html)
[ISimulation3DContactFeatureData::Exponent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Exponent.html)
[ISimulation3DContactFeatureData::Penetration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Penetration.html)
[ISimulation3DContactFeatureData::RestitutionCoefficient Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~RestitutionCoefficient.html)
[ISimulation3DContactFeatureData::Stiffness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Stiffness.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
