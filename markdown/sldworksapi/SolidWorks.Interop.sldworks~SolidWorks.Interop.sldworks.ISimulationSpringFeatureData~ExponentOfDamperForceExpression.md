---
title: "ExponentOfDamperForceExpression Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "ExponentOfDamperForceExpression"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.html"
---

# ExponentOfDamperForceExpression Property (ISimulationSpringFeatureData)

Gets or sets the exponent of the damper force expression for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExponentOfDamperForceExpression As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Integer

instance.ExponentOfDamperForceExpression = value

value = instance.ExponentOfDamperForceExpression
```

### C#

```csharp
System.int ExponentOfDamperForceExpression {get; set;}
```

### C++/CLI

```cpp
property System.int ExponentOfDamperForceExpression {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Exponent of the damper force expression

## VBA Syntax

See [SimulationSpringFeatureData::ExponentOfDamperForceExpression](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~ExponentOfDamperForceExpression.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::DampingConstant Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~DampingConstant.html)
[ISimulationSpringFeatureData::HasDamper Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~HasDamper.html)
[ISimulationSpringFeatureData::FreeAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeAngle.html)
[ISimulationSpringFeatureData::FreeLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeLength.html)
[ISimulationSpringFeatureData::SpringConstant Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SpringConstant.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
