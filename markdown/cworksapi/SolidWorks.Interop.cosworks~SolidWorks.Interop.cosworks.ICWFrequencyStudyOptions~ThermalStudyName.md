---
title: "ThermalStudyName Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "ThermalStudyName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~ThermalStudyName.html"
---

# ThermalStudyName Property (ICWFrequencyStudyOptions)

Gets or sets the thermal study used to obtain temperature values.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalStudyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.String

instance.ThermalStudyName = value

value = instance.ThermalStudyName
```

### C#

```csharp
System.string ThermalStudyName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ThermalStudyName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of a thermal study

## VBA Syntax

See [CWFrequencyStudyOptions::ThermalStudyName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~ThermalStudyName.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.

If the thermal study is a transient study, set [ICWFrequencyStudyOptions::TimeStep](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~TimeStep.html).

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
