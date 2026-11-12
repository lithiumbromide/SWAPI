---
title: "RandomVibrationFrequencyLowerLimit Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "RandomVibrationFrequencyLowerLimit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyLowerLimit.html"
---

# RandomVibrationFrequencyLowerLimit Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetRandomVibrationFrequencyLowerLimit2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyLowerLimit2.html) and [ICWDynamicStudyOptions::SetRandomVibrationFrequencyLowerLimit2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyLowerLimit2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property RandomVibrationFrequencyLowerLimit As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Double

instance.RandomVibrationFrequencyLowerLimit = value

value = instance.RandomVibrationFrequencyLowerLimit
```

### C#

```csharp
System.double RandomVibrationFrequencyLowerLimit {get; set;}
```

### C++/CLI

```cpp
property System.double RandomVibrationFrequencyLowerLimit {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Operating frequency lower limit

## VBA Syntax

See [CWDynamicStudyOptions::RandomVibrationFrequencyLowerLimit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~RandomVibrationFrequencyLowerLimit.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::RandomVibrationAnalysisMethod Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationAnalysisMethod.html)
[ICWDynamicStudyOptions::RandomVibrationBiasingParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationBiasingParameter.html)
[ICWDynamicStudyOptions::RandomVibrationCorrelationOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCorrelationOption.html)
[ICWDynamicStudyOptions::RandomVibrationCrossModeCutOffRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCrossModeCutOffRatio.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUnits.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::RandomVibrationGaussIntegrationOrder Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationGaussIntegrationOrder.html)
[ICWDynamicStudyOptions::RandomVibrationNoOfFrequencyPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationNoOfFrequencyPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
