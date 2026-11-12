---
title: "ThermalResults Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "ThermalResults"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~ThermalResults.html"
---

# ThermalResults Property (ICWFrequencyStudyOptions)

Gets or sets the source of temperatures in this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalResults As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.ThermalResults = value

value = instance.ThermalResults
```

### C#

```csharp
System.int ThermalResults {get; set;}
```

### C++/CLI

```cpp
property System.int ThermalResults {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Temperature source as defined by [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html)

## VBA Syntax

See [CWFrequencyStudyOptions::ThermalResults](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~ThermalResults.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)
[ICWFrequencyStudyOptions::ThermalStudyName Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~ThermalStudyName.html)
[ICWFrequencyStudyOptions::TimeStep Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~TimeStep.html)
[ICWFrequencyStudyOptions::FlowTemperatureFile Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FlowTemperatureFile.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
