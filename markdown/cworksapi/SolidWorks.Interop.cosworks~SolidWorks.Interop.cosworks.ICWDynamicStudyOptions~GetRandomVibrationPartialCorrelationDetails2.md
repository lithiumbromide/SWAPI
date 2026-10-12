---
title: "GetRandomVibrationPartialCorrelationDetails2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetRandomVibrationPartialCorrelationDetails2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationPartialCorrelationDetails2.html"
---

# GetRandomVibrationPartialCorrelationDetails2 Method (ICWDynamicStudyOptions)

Gets the partially correlated units, inside radius, and outside radius for the random vibration dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRandomVibrationPartialCorrelationDetails2( _
   ByRef NUnits As System.Integer, _
   ByRef DInRadius As System.Double, _
   ByRef DOutRadius As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NUnits As System.Integer
Dim DInRadius As System.Double
Dim DOutRadius As System.Double
Dim value As System.Integer

value = instance.GetRandomVibrationPartialCorrelationDetails2(NUnits, DInRadius, DOutRadius)
```

### C#

```csharp
System.int GetRandomVibrationPartialCorrelationDetails2(
   out System.int NUnits,
   out System.double DInRadius,
   out System.double DOutRadius
)
```

### C++/CLI

```cpp
System.int GetRandomVibrationPartialCorrelationDetails2(
   [Out] System.int NUnits,
   [Out] System.double DInRadius,
   [Out] System.double DOutRadius
)
```

### Parameters

- `NUnits`: Units as defined [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `DInRadius`: Inside radius
- `DOutRadius`: Outside radius

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetRandomVibrationPartialCorrelationDetails2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetRandomVibrationPartialCorrelationDetails2.html).

## Examples

[Create Linear Dynamic Random Vibration Study (VBA)](Create_Dynamic_Random_Vibration_Study_Example_VB.htm)
[Create Linear Dynamic Random Vibration Study (VB.NET)](Create_Dynamic_Random_Vibration_Study_Example_VBNET.htm)
[Create Linear Dynamic Random Vibration Study (C#)](Create_Dynamic_Random_Vibration_Study_Example_CSharp.htm)

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetRandomVibrationPartialCorrelationDetails2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationPartialCorrelationDetails2.html)
[ICWDynamicStudyOptions::GetRandomVibrationAnalysisMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationAnalysisMethod2.html)
[ICWDynamicStudyOptions::GetRandomVibrationBiasingParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationBiasingParameter2.html)
[ICWDynamicStudyOptions::GetRandomVibrationCorrelationOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationCorrelationOption2.html)
[ICWDynamicStudyOptions::GetRandomVibrationCrossModeCutOffRatio2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationCrossModeCutOffRatio2.html)
[ICWDynamicStudyOptions::GetRandomVibrationFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::GetRandomVibrationFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyUnits2.html)
[ICWDynamicStudyOptions::GetRandomVibrationFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::GetRandomVibrationGaussIntegrationOrder2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationGaussIntegrationOrder2.html)
[ICWDynamicStudyOptions::GetRandomVibrationNoOfFrequencyPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationNoOfFrequencyPoints2.html)
[ICWDynamicStudyOptions::SetRandomVibrationAnalysisMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationAnalysisMethod2.html)
[ICWDynamicStudyOptions::SetRandomVibrationBiasingParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationBiasingParameter2.html)
[ICWDynamicStudyOptions::SetRandomVibrationCorrelationOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationCorrelationOption2.html)
[ICWDynamicStudyOptions::SetRandomVibrationCrossModeCutOffRatio2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationCrossModeCutOffRatio2.html)
[ICWDynamicStudyOptions::SetRandomVibrationFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::SetRandomVibrationFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyUnits2.html)
[ICWDynamicStudyOptions::SetRandomVibrationFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::SetRandomVibrationGaussIntegrationOrder2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationGaussIntegrationOrder2.html)
[ICWDynamicStudyOptions::SetRandomVibrationNoOfFrequencyPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationNoOfFrequencyPoints2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
