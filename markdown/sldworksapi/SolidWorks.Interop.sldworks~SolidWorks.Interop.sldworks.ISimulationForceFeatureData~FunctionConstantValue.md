---
title: "FunctionConstantValue Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "FunctionConstantValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionConstantValue.html"
---

# FunctionConstantValue Property (ISimulationForceFeatureData)

Gets or sets the function constant value for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FunctionConstantValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.Double

instance.FunctionConstantValue = value

value = instance.FunctionConstantValue
```

### C#

```csharp
System.double FunctionConstantValue {get; set;}
```

### C++/CLI

```cpp
property System.double FunctionConstantValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Function constant value

## VBA Syntax

See [SimulationForceFeatureData::FunctionConstantValue](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~FunctionConstantValue.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::GetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::GetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionStepValues.html)
[ISimulationForceFeatureData::SetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::SetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionStepValues.html)
[ISimulationForceFeatureData::FunctionExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionExpression.html)
[ISimulationForceFeatureData::ForceFunctionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceFunctionType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
