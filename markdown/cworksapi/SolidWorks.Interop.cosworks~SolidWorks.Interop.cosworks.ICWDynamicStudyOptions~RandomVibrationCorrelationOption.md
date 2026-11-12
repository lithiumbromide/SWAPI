---
title: "RandomVibrationCorrelationOption Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "RandomVibrationCorrelationOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCorrelationOption.html"
---

# RandomVibrationCorrelationOption Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetRandomVibrationCorrelationOption2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationCorrelationOption2.html) and [ICWDynamicStudyOptions::SetRandomVibrationCorrelationOption2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationCorrelationOption2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property RandomVibrationCorrelationOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.RandomVibrationCorrelationOption = value

value = instance.RandomVibrationCorrelationOption
```

### C#

```csharp
System.int RandomVibrationCorrelationOption {get; set;}
```

### C++/CLI

```cpp
property System.int RandomVibrationCorrelationOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Correlation type as defined in [swsRandomVibrationCorrelationOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRandomVibrationCorrelationOption_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::RandomVibrationCorrelationOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~RandomVibrationCorrelationOption.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::RandomVibrationAnalysisMethod Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationAnalysisMethod.html)
[ICWDynamicStudyOptions::RandomVibrationBiasingParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationBiasingParameter.html)
[ICWDynamicStudyOptions::RandomVibrationCrossModeCutOffRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCrossModeCutOffRatio.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyLowerLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyLowerLimit.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUnits.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::RandomVibrationGaussIntegrationOrder Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationGaussIntegrationOrder.html)
[ICWDynamicStudyOptions::RandomVibrationNoOfFrequencyPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationNoOfFrequencyPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
