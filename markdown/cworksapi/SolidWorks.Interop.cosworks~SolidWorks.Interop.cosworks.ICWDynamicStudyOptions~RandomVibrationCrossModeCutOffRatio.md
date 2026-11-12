---
title: "RandomVibrationCrossModeCutOffRatio Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "RandomVibrationCrossModeCutOffRatio"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCrossModeCutOffRatio.html"
---

# RandomVibrationCrossModeCutOffRatio Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetRandomVibrationCrossModeCutOffRatio2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationCrossModeCutOffRatio2.html) and [ICWDyamicStudyOptions::SetRandomVibrationCrossModeCutOffRatio2.](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationCrossModeCutOffRatio2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property RandomVibrationCrossModeCutOffRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Double

instance.RandomVibrationCrossModeCutOffRatio = value

value = instance.RandomVibrationCrossModeCutOffRatio
```

### C#

```csharp
System.double RandomVibrationCrossModeCutOffRatio {get; set;}
```

### C++/CLI

```cpp
property System.double RandomVibrationCrossModeCutOffRatio {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Cross-mode cut-off ratio

## VBA Syntax

See [CWDynamicStudyOptions::RandomVibrationCrossModeCutOffRatio](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~RandomVibrationCrossModeCutOffRatio.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::RandomVibrationAnalysisMethod Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationAnalysisMethod.html)
[ICWDynamicStudyOptions::RandomVibrationBiasingParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationBiasingParameter.html)
[ICWDynamicStudyOptions::RandomVibrationCorrelationOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCorrelationOption.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyLowerLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyLowerLimit.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUnits.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::RandomVibrationGaussIntegrationOrder Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationGaussIntegrationOrder.html)
[ICWDynamicStudyOptions::RandomVibrationNoOfFrequencyPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationNoOfFrequencyPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
