---
title: "ThermalStudyName Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "ThermalStudyName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ThermalStudyName.html"
---

# ThermalStudyName Property (ICWBucklingStudyOptions)

Gets or sets the thermal study used to obtain temperature values.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalStudyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::ThermalStudyName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~ThermalStudyName.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWBucklingStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.

If the thermal study is transient, set [ICWBucklingStudyOptions::TimeStep](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~TimeStep.html).

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
