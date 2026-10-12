---
title: "ForceFunctionType Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "ForceFunctionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceFunctionType.html"
---

# ForceFunctionType Property (ISimulationForceFeatureData)

Gets or sets the type of function for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ForceFunctionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.Integer

instance.ForceFunctionType = value

value = instance.ForceFunctionType
```

### C#

```csharp
System.int ForceFunctionType {get; set;}
```

### C++/CLI

```cpp
property System.int ForceFunctionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of function as defined in [swSimulationForceFunctionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationForceFunctionType_e.html)

## VBA Syntax

See [SimulationForceFeatureData::ForceFunctionType](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~ForceFunctionType.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::GetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::GetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionStepValues.html)
[ISimulationForceFeatureData::SetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::SetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionStepValues.html)
[ISimulationForceFeatureData::FunctionConstantValue Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionConstantValue.html)
[ISimulationForceFeatureData::FunctionExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionExpression.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
