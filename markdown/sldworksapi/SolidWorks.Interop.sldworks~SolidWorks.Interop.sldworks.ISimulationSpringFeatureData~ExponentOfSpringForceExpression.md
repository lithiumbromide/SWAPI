---
title: "ExponentOfSpringForceExpression Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "ExponentOfSpringForceExpression"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfSpringForceExpression.html"
---

# ExponentOfSpringForceExpression Property (ISimulationSpringFeatureData)

Gets or sets the exponent of the spring force expression for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExponentOfSpringForceExpression As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Integer

instance.ExponentOfSpringForceExpression = value

value = instance.ExponentOfSpringForceExpression
```

### C#

```csharp
System.int ExponentOfSpringForceExpression {get; set;}
```

### C++/CLI

```cpp
property System.int ExponentOfSpringForceExpression {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Exponent of the spring force expression

## VBA Syntax

See [SimulationSpringFeatureData::ExponentOfSpringForceExpression](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~ExponentOfSpringForceExpression.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::SpringConstant Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SpringConstant.html)
[ISimulationSpringFeatureData::FreeAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeAngle.html)
[ISimulationSpringFeatureData::FreeLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeLength.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
