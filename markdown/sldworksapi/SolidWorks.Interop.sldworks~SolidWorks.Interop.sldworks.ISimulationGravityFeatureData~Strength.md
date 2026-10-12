---
title: "Strength Property (ISimulationGravityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationGravityFeatureData"
member: "Strength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData~Strength.html"
---

# Strength Property (ISimulationGravityFeatureData)

Gets or sets the gravitational strength.

## Syntax

### Visual Basic (Declaration)

```vb
Property Strength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationGravityFeatureData
Dim value As System.Double

instance.Strength = value

value = instance.Strength
```

### C#

```csharp
System.double Strength {get; set;}
```

### C++/CLI

```cpp
property System.double Strength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gravitational strength

## VBA Syntax

See [SimulationGravityFeatureData::Strength](ms-its:sldworksapivb6.chm::/sldworks~SimulationGravityFeatureData~Strength.html).

## Examples

See the [ISimulationGravityFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html) examples.

## See Also

[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.html)
[ISimulationGravityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
