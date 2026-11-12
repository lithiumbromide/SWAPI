---
title: "FunctionExpression Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "FunctionExpression"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionExpression.html"
---

# FunctionExpression Property (ISimulationForceFeatureData)

Gets or sets the expression function for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FunctionExpression As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.String

instance.FunctionExpression = value

value = instance.FunctionExpression
```

### C#

```csharp
System.string FunctionExpression {get; set;}
```

### C++/CLI

```cpp
property System.String^ FunctionExpression {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Expression function in document units

## VBA Syntax

See [SimulationForceFeatureData::FunctionExpression](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~FunctionExpression.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::GetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::GetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionStepValues.html)
[ISimulationForceFeatureData::SetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::SetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionStepValues.html)
[ISimulationForceFeatureData::FunctionConstantValue Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionConstantValue.html)
[ISimulationForceFeatureData::ForceFunctionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceFunctionType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
