---
title: "ThermalStudyName Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "ThermalStudyName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalStudyName.html"
---

# ThermalStudyName Property (ICWNonLinearStudyOptions)

Gets or sets the thermal study used to obtain temperature values.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalStudyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
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

See [CWNonLinearStudyOptions::ThermalStudyName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~ThermalStudyName.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWNonLinearStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.

If this property sets a transient thermal study and:

| If ICWNonLinearStudyOptions::CheckUseTempFromThermalStudy is set to... | Then... |
| --- | --- |
| 0 | Use ICWNonLinearStudyOptions::TimeStep to set the time step at which to import a temperature to use from the transient thermal study. |
| 1 | The corresponding temperature in the transient thermal study at each nonlinear step is used. |

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
