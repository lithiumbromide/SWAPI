---
title: "DampingConstant Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "DampingConstant"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~DampingConstant.html"
---

# DampingConstant Property (ISimulationSpringFeatureData)

Gets or sets the damping constant for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DampingConstant As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Double

instance.DampingConstant = value

value = instance.DampingConstant
```

### C#

```csharp
System.double DampingConstant {get; set;}
```

### C++/CLI

```cpp
property System.double DampingConstant {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Damping constant

## VBA Syntax

See [SimulationSpringFeatureData::DampingConstant](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~DampingConstant.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::HasDamper Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~HasDamper.html)
[ISimulationSpringFeatureData::ExponentOfDamperForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
