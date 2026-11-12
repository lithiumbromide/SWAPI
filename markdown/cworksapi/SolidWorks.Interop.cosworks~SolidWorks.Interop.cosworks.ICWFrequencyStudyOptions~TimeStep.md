---
title: "TimeStep Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "TimeStep"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~TimeStep.html"
---

# TimeStep Property (ICWFrequencyStudyOptions)

Gets or sets the time step for which to import a single temperature from a transient thermal study.

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeStep As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.TimeStep = value

value = instance.TimeStep
```

### C#

```csharp
System.int TimeStep {get; set;}
```

### C++/CLI

```cpp
property System.int TimeStep {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Time step for which to import a single temperature from a transient thermal study

## VBA Syntax

See [CWFrequencyStudyOptions::TimeStep](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~TimeStep.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property is valid only if:

- [ICWFrequencyStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.
- [ICWFrequencyStudyOptions::ThermalStudyName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~ThermalStudyName.html) is specified and is a transient thermal study.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
