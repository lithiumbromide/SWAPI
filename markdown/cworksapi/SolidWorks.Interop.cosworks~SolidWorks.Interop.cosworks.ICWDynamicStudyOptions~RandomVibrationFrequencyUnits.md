---
title: "RandomVibrationFrequencyUnits Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "RandomVibrationFrequencyUnits"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUnits.html"
---

# RandomVibrationFrequencyUnits Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetRandomVibrationFrequencyUnits2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationFrequencyUnits2.html) and [ICWDynamicStudyOptions::SetRandomVibrationFrequencyUnits2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationFrequencyUnits2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property RandomVibrationFrequencyUnits As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.RandomVibrationFrequencyUnits = value

value = instance.RandomVibrationFrequencyUnits
```

### C#

```csharp
System.int RandomVibrationFrequencyUnits {get; set;}
```

### C++/CLI

```cpp
property System.int RandomVibrationFrequencyUnits {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units of operating frequency as defined in [swsFrequencyUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyUnit_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::RandomVibrationFrequencyUnits](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~RandomVibrationFrequencyUnits.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::RandomVibrationAnalysisMethod Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationAnalysisMethod.html)
[ICWDynamicStudyOptions::RandomVibrationBiasingParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationBiasingParameter.html)
[ICWDynamicStudyOptions::RandomVibrationCorrelationOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCorrelationOption.html)
[ICWDynamicStudyOptions::RandomVibrationCrossModeCutOffRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCrossModeCutOffRatio.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyLowerLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyLowerLimit.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::RandomVibrationGaussIntegrationOrder Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationGaussIntegrationOrder.html)
[ICWDynamicStudyOptions::RandomVibrationNoOfFrequencyPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationNoOfFrequencyPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
