---
title: "SetRandomVibrationFrequencyLowerLimit2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetRandomVibrationFrequencyLowerLimit2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyLowerLimit2.html"
---

# SetRandomVibrationFrequencyLowerLimit2 Method (ICWDynamicStudyOptions)

Sets the lower limit of the operating frequency of the random vibration dynamic study

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRandomVibrationFrequencyLowerLimit2( _
   ByVal DLowerLimit As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DLowerLimit As System.Double
Dim value As System.Integer

value = instance.SetRandomVibrationFrequencyLowerLimit2(DLowerLimit)
```

### C#

```csharp
System.int SetRandomVibrationFrequencyLowerLimit2(
   System.double DLowerLimit
)
```

### C++/CLI

```cpp
System.int SetRandomVibrationFrequencyLowerLimit2(
   System.double DLowerLimit
)
```

### Parameters

- `DLowerLimit`: Operating frequency lower limit

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetRandomVibrationFrequencyLowerLimit2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetRandomVibrationFrequencyLowerLimit2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetRandomVibrationFrequencyLowerLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyLowerLimit2.html)
[ICWDynamicStudyOptions::SetRandomVibrationAnalysisMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationAnalysisMethod2.html)
[ICWDynamicStudyOptions::SetRandomVibrationBiasingParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationBiasingParameter2.html)
[ICWDynamicStudyOptions::SetRandomVibrationCorrelationOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationCorrelationOption2.html)
[ICWDynamicStudyOptions::SetRandomVibrationCrossModeCutOffRatio2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationCrossModeCutOffRatio2.html)
[ICWDynamicStudyOptions::SetRandomVibrationFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyUnits2.html)
[ICWDynamicStudyOptions::SetRandomVibrationFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::SetRandomVibrationGaussIntegrationOrder2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationGaussIntegrationOrder2.html)
[ICWDynamicStudyOptions::SetRandomVibrationNoOfFrequencyPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationNoOfFrequencyPoints2.html)
[ICWDynamicStudyOptions::SetRandomVibrationPartialCorrelationDetails2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationPartialCorrelationDetails2.html)
[ICWDynamicStudyOptions::GetRandomVibrationAnalysisMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationAnalysisMethod2.html)
[ICWDynamicStudyOptions::GetRandomVibrationBiasingParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationBiasingParameter2.html)
[ICWDynamicStudyOptions::GetRandomVibrationCorrelationOption2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationCorrelationOption2.html)
[ICWDynamicStudyOptions::GetRandomVibrationCrossModeCutOffRatio2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationCrossModeCutOffRatio2.html)
[ICWDynamicStudyOptions::GetRandomVibrationFrequencyUnits2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyUnits2.html)
[ICWDynamicStudyOptions::GetRandomVibrationFrequencyUpperLimit2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyUpperLimit2.html)
[ICWDynamicStudyOptions::GetRandomVibrationGaussIntegrationOrder2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationGaussIntegrationOrder2.html)
[ICWDynamicStudyOptions::GetRandomVibrationNoOfFrequencyPoints2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationNoOfFrequencyPoints2.html)
[ICWDynamicStudyOptions::GetRandomVibrationPartialCorrelationDetails2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationPartialCorrelationDetails2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
