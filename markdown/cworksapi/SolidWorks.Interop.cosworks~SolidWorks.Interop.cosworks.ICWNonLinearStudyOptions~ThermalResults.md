---
title: "ThermalResults Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "ThermalResults"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalResults.html"
---

# ThermalResults Property (ICWNonLinearStudyOptions)

Gets or sets the source of temperatures in this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalResults As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
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

See [CWNonLinearStudyOptions::ThermalResults](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~ThermalResults.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::ThermalStudyName Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalStudyName.html)
[ICWNonLinearStudyOptions::TimeStep Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeStep.html)
[ICWNonLinearStudyOptions::CheckUseTempFromThermalStudy Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckUseTempFromThermalStudy.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
