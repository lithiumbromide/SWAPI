---
title: "Units Property (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "Units"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~Units.html"
---

# Units Property (ICWDynamicInitialCondition)

Gets or sets the units of this initial condition.

## Syntax

### Visual Basic (Declaration)

```vb
Property Units As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim value As System.Integer

instance.Units = value

value = instance.Units
```

### C#

```csharp
System.int Units {get; set;}
```

### C++/CLI

```cpp
property System.int Units {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- Value as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html), if [ICWDynamicInitialCondition::InitialConditionType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicInitialCondition~InitialConditionType.html) = swsDynamicInitialConditionType_e.swsDynamicInitialConditionType_Displacement
- Value as defined in [swsVelocityUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsVelocityUnit_e.html), if ICWDynamicInitialCondition::InitialConditionType = swsDynamicInitialConditionType_e.swsDynamicInitialConditionType_Velocity
- Value as defined in [swsAccelerationUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAccelerationUnit_e.html), if ICWDynamicInitialCondition::InitialConditionType = swsDynamicInitialConditionType_e.swsDynamicInitialConditionType_Acceleration

## VBA Syntax

See [CWDynamicInitialCondition::Units](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~Units.html).

## Examples

See the [ICWDynamicInitialCondition](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html) examples.

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
