---
title: "TimeStep Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "TimeStep"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~TimeStep.html"
---

# TimeStep Property (ICWBucklingStudyOptions)

Gets or sets the time step from which to import a single temperature from a transient thermal study.

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeStep As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

Time step from which to import a single temperature

## VBA Syntax

See [CWBucklingStudyOptions::TimeStep](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~TimeStep.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## Remarks

This property is valid only if:

- [ICWBucklingStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.
- [ICWBucklingStudyOptions::ThermalStudyName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ThermalStudyName.html) is specified and is a transient thermal study.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
