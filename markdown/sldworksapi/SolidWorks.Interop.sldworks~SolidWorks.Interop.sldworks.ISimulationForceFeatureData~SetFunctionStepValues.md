---
title: "SetFunctionStepValues Method (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "SetFunctionStepValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionStepValues.html"
---

# SetFunctionStepValues Method (ISimulationForceFeatureData)

Sets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFunctionStepValues( _
   ByVal F1InitialValue As System.Double, _
   ByVal T1StartStepTime As System.Double, _
   ByVal F2InitialValue As System.Double, _
   ByVal T2EndStepTime As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim F1InitialValue As System.Double
Dim T1StartStepTime As System.Double
Dim F2InitialValue As System.Double
Dim T2EndStepTime As System.Double
Dim value As System.Boolean

value = instance.SetFunctionStepValues(F1InitialValue, T1StartStepTime, F2InitialValue, T2EndStepTime)
```

### C#

```csharp
System.bool SetFunctionStepValues(
   System.double F1InitialValue,
   System.double T1StartStepTime,
   System.double F2InitialValue,
   System.double T2EndStepTime
)
```

### C++/CLI

```cpp
System.bool SetFunctionStepValues(
   System.double F1InitialValue,
   System.double T1StartStepTime,
   System.double F2InitialValue,
   System.double T2EndStepTime
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `F1InitialValue`: Value of the function before the step
- `T1StartStepTime`: Time at which the step begins
- `F2InitialValue`: Value of the function after the step
- `T2EndStepTime`: Time at which the step ends

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [SimulationForceFeatureData::SetFunctionStepValues](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~SetFunctionStepValues.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::GetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionStepValues.html)
[ISimulationForceFeatureData::GetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::SetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::FunctionConstantValue Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionConstantValue.html)
[ISimulationForceFeatureData::FunctionExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionExpression.html)
[ISimulationForceFeatureData::ForceFunctionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceFunctionType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
