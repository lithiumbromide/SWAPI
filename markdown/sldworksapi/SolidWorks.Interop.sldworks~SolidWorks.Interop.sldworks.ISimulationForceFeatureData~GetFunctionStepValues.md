---
title: "GetFunctionStepValues Method (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "GetFunctionStepValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionStepValues.html"
---

# GetFunctionStepValues Method (ISimulationForceFeatureData)

Gets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFunctionStepValues( _
   ByRef F1InitialValue As System.Double, _
   ByRef T1StartStepTime As System.Double, _
   ByRef F2InitialValue As System.Double, _
   ByRef T2EndStepTime As System.Double _
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

value = instance.GetFunctionStepValues(F1InitialValue, T1StartStepTime, F2InitialValue, T2EndStepTime)
```

### C#

```csharp
System.bool GetFunctionStepValues(
   out System.double F1InitialValue,
   out System.double T1StartStepTime,
   out System.double F2InitialValue,
   out System.double T2EndStepTime
)
```

### C++/CLI

```cpp
System.bool GetFunctionStepValues(
   [Out] System.double F1InitialValue,
   [Out] System.double T1StartStepTime,
   [Out] System.double F2InitialValue,
   [Out] System.double T2EndStepTime
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

See [SimulationForceFeatureData::GetFunctionStepValues](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~GetFunctionStepValues.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::SetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionStepValues.html)
[ISimulationForceFeatureData::GetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::FunctionConstantValue Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionConstantValue.html)
[ISimulationForceFeatureData::FunctionExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionExpression.html)
[ISimulationForceFeatureData::ForceFunctionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceFunctionType.html)
[ISimulationForceFeatureData::SetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionHarmonicValues.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
