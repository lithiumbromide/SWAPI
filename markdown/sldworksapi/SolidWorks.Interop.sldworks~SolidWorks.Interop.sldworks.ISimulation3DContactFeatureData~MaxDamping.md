---
title: "MaxDamping Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "MaxDamping"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~MaxDamping.html"
---

# MaxDamping Property (ISimulation3DContactFeatureData)

Gets or sets the maximum damping coefficient of the boundary of interaction in a 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxDamping As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim value As System.Double

instance.MaxDamping = value

value = instance.MaxDamping
```

### C#

```csharp
System.double MaxDamping {get; set;}
```

### C++/CLI

```cpp
property System.double MaxDamping {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum damping coefficient of the boundary of interaction

## VBA Syntax

See [Simulation3DContactFeatureData::MaxDamping](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~MaxDamping.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## Remarks

Available only when [ISimulation3DContactFeatureData::UseRestitutionCoefficient](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation3DContactFeatureData~UseRestitutionCoefficient.html) and [ISimulation3DContactFeatureData::SpecifyMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~SpecifyMaterial.html) are both false.

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
