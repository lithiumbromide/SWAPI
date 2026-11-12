---
title: "TimeStep Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "TimeStep"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeStep.html"
---

# TimeStep Property (ICWNonLinearStudyOptions)

Gets or sets the time step at which to import a single temperature from a transient thermal study.

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeStep As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
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

Time step at which to import a single temperature from a transient thermal study

## VBA Syntax

See [CWNonLinearStudyOptions::TimeStep](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~TimeStep.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

This property is valid only if:

- [ICWNonLinearStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.
- [ICWNonLinearStudyOptions::ThermalStudyName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalStudyName.html) is specified and is a transient thermal study.
- [ICWNonLinearStudyOptions::CheckUseTempFromThermalStudy](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckUseTempFromThermalStudy.html) is set to 0.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
