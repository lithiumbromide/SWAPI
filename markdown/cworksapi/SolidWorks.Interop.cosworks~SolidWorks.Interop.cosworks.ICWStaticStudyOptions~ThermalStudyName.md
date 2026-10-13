---
title: "ThermalStudyName Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "ThermalStudyName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ThermalStudyName.html"
---

# ThermalStudyName Property (ICWStaticStudyOptions)

Gets or sets the thermal study from which to import temperature values for this static study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalStudyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::ThermalStudyName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~ThermalStudyName.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

This property is valid only if [ICWStaticStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.

If this property sets a transient thermal study, then use [ICWStaticStudyOptions::TimeStep](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~TimeStep.html) to set the time step of the thermal study at which to import a single temperature.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
