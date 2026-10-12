---
title: "SetRandomVibrationFrequencyUnits2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetRandomVibrationFrequencyUnits2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyUnits2.html"
---

# SetRandomVibrationFrequencyUnits2 Method (ICWDynamicStudyOptions)

Sets the units of the operating frequency of the random vibration dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRandomVibrationFrequencyUnits2( _
   ByVal NUnits As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NUnits As System.Integer
Dim value As System.Integer

value = instance.SetRandomVibrationFrequencyUnits2(NUnits)
```

### C#

```csharp
System.int SetRandomVibrationFrequencyUnits2(
   System.int NUnits
)
```

### C++/CLI

```cpp
System.int SetRandomVibrationFrequencyUnits2(
   System.int NUnits
)
```

### Parameters

- `NUnits`: Units of operating frequency as defined in [swsFrequencyUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyUnit_e.html)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetRandomVibrationFrequencyUnits2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetRandomVibrationFrequencyUnits2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetRandomVibrationFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyUnits2.html)
[ICWDynamicStudyOptions::SetRandomVibrationAnalysisMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationAnalysisMethod2.html)
[ICWDynamicStudyOptions::SetRandomVibrationBiasingParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationBiasingParameter2.html)
[ICWDynamicStudyOptions::SetRandomVibrationCorrelationOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationCorrelationOption2.html)
[ICWDynamicStudyOptions::SetRandomVibrationCrossModeCutOffRatio2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationCrossModeCutOffRatio2.html)
[ICWDynamicStudyOptions::SetRandomVibrationFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::SetRandomVibrationFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::SetRandomVibrationGaussIntegrationOrder2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationGaussIntegrationOrder2.html)
[ICWDynamicStudyOptions::SetRandomVibrationNoOfFrequencyPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationNoOfFrequencyPoints2.html)
[ICWDynamicStudyOptions::SetRandomVibrationPartialCorrelationDetails2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationPartialCorrelationDetails2.html)
[ICWDynamicStudyOptions::GetRandomVibrationAnalysisMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationAnalysisMethod2.html)
[ICWDynamicStudyOptions::GetRandomVibrationBiasingParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationBiasingParameter2.html)
[ICWDynamicStudyOptions::GetRandomVibrationCorrelationOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationCorrelationOption2.html)
[ICWDynamicStudyOptions::GetRandomVibrationCrossModeCutOffRatio2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationCrossModeCutOffRatio2.html)
[ICWDynamicStudyOptions::GetRandomVibrationFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::GetRandomVibrationFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::GetRandomVibrationGaussIntegrationOrder2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationGaussIntegrationOrder2.html)
[ICWDynamicStudyOptions::GetRandomVibrationNoOfFrequencyPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationNoOfFrequencyPoints2.html)
[ICWDynamicStudyOptions::GetRandomVibrationPartialCorrelationDetails2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationPartialCorrelationDetails2.html)

## Availability

SOLIDWORKS Simulation API 2105 SP0
