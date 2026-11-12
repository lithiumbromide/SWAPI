---
title: "ExponentOfDamperForceExpression Property (ISimulationDamperFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationDamperFeatureData"
member: "ExponentOfDamperForceExpression"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData~ExponentOfDamperForceExpression.html"
---

# ExponentOfDamperForceExpression Property (ISimulationDamperFeatureData)

Gets or sets the exponent for the functional expression for this damper feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExponentOfDamperForceExpression As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationDamperFeatureData
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

Exponent for the functional expression

## VBA Syntax

See [SimulationDamperFeatureData::ExponentOfDamperForceExpression](ms-its:sldworksapivb6.chm::/sldworks~SimulationDamperFeatureData~ExponentOfDamperForceExpression.html).

## See Also

[ISimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.html)
[ISimulationDamperFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
