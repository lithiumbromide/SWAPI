---
title: "Stiffness Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "Stiffness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Stiffness.html"
---

# Stiffness Property (ISimulation3DContactFeatureData)

Gets or sets the stiffness at the boundary of interaction between the two parts in a 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Stiffness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim value As System.Double

instance.Stiffness = value

value = instance.Stiffness
```

### C#

```csharp
System.double Stiffness {get; set;}
```

### C++/CLI

```cpp
property System.double Stiffness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Stiffness at the boundary of interaction

## VBA Syntax

See [Simulation3DContactFeatureData::Stiffness](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~Stiffness.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## Remarks

Available only when [ISimulation3DContactFeatureData::UseRestitutionCoefficient](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation3DContactFeatureData~UseRestitutionCoefficient.html) and [ISimulation3DContactFeatureData::SpecifyMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~SpecifyMaterial.html) are both false.

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
