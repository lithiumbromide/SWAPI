---
title: "ThermalResults Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "ThermalResults"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ThermalResults.html"
---

# ThermalResults Property (ICWStaticStudyOptions)

Gets or sets the source of temperatures in this static study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalResults As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::ThermalResults](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~ThermalResults.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::ThermalStudyName Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ThermalStudyName.html)
[ICWStaticStudyOptions::TimeStep Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~TimeStep.html)
[ICWStaticStudyOptions::FlowTemperatureFile Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~FlowTemperatureFile.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
