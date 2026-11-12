---
title: "TimeStep Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "TimeStep"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~TimeStep.html"
---

# TimeStep Property (ICWStaticStudyOptions)

Gets or sets the time step at which to import a single temperature from a transient thermal study.

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeStep As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::TimeStep](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~TimeStep.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

This property is valid only if:

- [ICWStaticStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.
- [ICWStaticStudyOptions::ThermalStudyName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ThermalStudyName.html) is specified and is a transient thermal study.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
