---
title: "SetFunctionHarmonicValues Method (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "SetFunctionHarmonicValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionHarmonicValues.html"
---

# SetFunctionHarmonicValues Method (ISimulationForceFeatureData)

Sets the harmonic function values for this Force feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFunctionHarmonicValues( _
   ByVal Amplitude As System.Double, _
   ByVal Frequency As System.Double, _
   ByVal Average As System.Double, _
   ByVal PhaseShift As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim Amplitude As System.Double
Dim Frequency As System.Double
Dim Average As System.Double
Dim PhaseShift As System.Double
Dim value As System.Boolean

value = instance.SetFunctionHarmonicValues(Amplitude, Frequency, Average, PhaseShift)
```

### C#

```csharp
System.bool SetFunctionHarmonicValues(
   System.double Amplitude,
   System.double Frequency,
   System.double Average,
   System.double PhaseShift
)
```

### C++/CLI

```cpp
System.bool SetFunctionHarmonicValues(
   System.double Amplitude,
   System.double Frequency,
   System.double Average,
   System.double PhaseShift
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Amplitude`: Amplitude of the function measured peak to peak
- `Frequency`: Frequency of the function
- `Average`: Average value of the function; the function oscillates about this value
- `PhaseShift`: Phase shift for the function

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [SimulationForceFeatureData::SetFunctionHarmonicValues](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~SetFunctionHarmonicValues.html).

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)
[ISimulationForceFeatureData::GetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionHarmonicValues.html)
[ISimulationForceFeatureData::GetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionStepValues.html)
[ISimulationForceFeatureData::SetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionStepValues.html)
[ISimulationForceFeatureData::FunctionConstantValue Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionConstantValue.html)
[ISimulationForceFeatureData::FunctionExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionExpression.html)
[ISimulationForceFeatureData::ForceFunctionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceFunctionType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
