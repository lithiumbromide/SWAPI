---
title: "RandomVibrationGaussIntegrationOrder Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "RandomVibrationGaussIntegrationOrder"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationGaussIntegrationOrder.html"
---

# RandomVibrationGaussIntegrationOrder Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetRandomVibrationGaussIntegrationOrder2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationGaussIntegrationOrder2.html) and [ICWDynamicStudyOptions::SetRandomVibrationGaussIntegrationOrder2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationGaussIntegrationOrder2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property RandomVibrationGaussIntegrationOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.RandomVibrationGaussIntegrationOrder = value

value = instance.RandomVibrationGaussIntegrationOrder
```

### C#

```csharp
System.int RandomVibrationGaussIntegrationOrder {get; set;}
```

### C++/CLI

```cpp
property System.int RandomVibrationGaussIntegrationOrder {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Gauss integration order as defined in [swsGaussIntegrationOrder_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsGaussIntegrationOrder_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::RandomVibrationGaussIntegrationOrder](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~RandomVibrationGaussIntegrationOrder.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::RandomVibrationAnalysisMethod Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationAnalysisMethod.html)
[ICWDynamicStudyOptions::RandomVibrationBiasingParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationBiasingParameter.html)
[ICWDynamicStudyOptions::RandomVibrationCorrelationOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCorrelationOption.html)
[ICWDynamicStudyOptions::RandomVibrationCrossModeCutOffRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationCrossModeCutOffRatio.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyLowerLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyLowerLimit.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUnits.html)
[ICWDynamicStudyOptions::RandomVibrationFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::RandomVibrationNoOfFrequencyPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~RandomVibrationNoOfFrequencyPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
