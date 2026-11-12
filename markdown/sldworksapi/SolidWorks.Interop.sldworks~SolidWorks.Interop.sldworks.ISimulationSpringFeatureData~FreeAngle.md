---
title: "FreeAngle Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "FreeAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeAngle.html"
---

# FreeAngle Property (ISimulationSpringFeatureData)

Gets or sets the free angle for the functional expression for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FreeAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Double

instance.FreeAngle = value

value = instance.FreeAngle
```

### C#

```csharp
System.double FreeAngle {get; set;}
```

### C++/CLI

```cpp
property System.double FreeAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Free angle

## VBA Syntax

See [SimulationSpringFeatureData::FreeAngle](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~FreeAngle.html).

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::ExponentOfDamperForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.html)
[ISimulationSpringFeatureData::ExponentOfSpringForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfSpringForceExpression.html)
[ISimulationSpringFeatureData::FreeLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeLength.html)
[ISimulationSpringFeatureData::SpringConstant Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SpringConstant.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
