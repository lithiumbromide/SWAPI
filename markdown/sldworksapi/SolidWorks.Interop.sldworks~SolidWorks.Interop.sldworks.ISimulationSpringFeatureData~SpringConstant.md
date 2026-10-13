---
title: "SpringConstant Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "SpringConstant"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SpringConstant.html"
---

# SpringConstant Property (ISimulationSpringFeatureData)

Gets or sets the strength of this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpringConstant As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Double

instance.SpringConstant = value

value = instance.SpringConstant
```

### C#

```csharp
System.double SpringConstant {get; set;}
```

### C++/CLI

```cpp
property System.double SpringConstant {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Strength

## VBA Syntax

See [SimulationSpringFeatureData::SpringConstant](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~SpringConstant.html).

## Remarks

Springs apply a force to a component. A spring with a higher spring constant moves a component faster than a spring with a lower spring constant. A component with a smaller mass moves faster than a component with a larger mass when acted upon by an equal strength spring.

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::ExponentOfDamperForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.html)
[ISimulationSpringFeatureData::ExponentOfSpringForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfSpringForceExpression.html)
[ISimulationSpringFeatureData::FreeAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeAngle.html)
[ISimulationSpringFeatureData::FreeLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeLength.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
