---
title: "CheckUseTempFromThermalStudy Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "CheckUseTempFromThermalStudy"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckUseTempFromThermalStudy.html"
---

# CheckUseTempFromThermalStudy Property (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::CheckUseTempFromThermalStudy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckUseTempFromThermalStudy2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckUseTempFromThermalStudy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.CheckUseTempFromThermalStudy = value

value = instance.CheckUseTempFromThermalStudy
```

### C#

```csharp
System.int CheckUseTempFromThermalStudy {get; set;}
```

### C++/CLI

```cpp
property System.int CheckUseTempFromThermalStudy {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use the temperature from the corresponding time of a transient thermal analysis at each nonlinear time step, 0 to not

## VBA Syntax

See [CWNonLinearStudyOptions::CheckUseTempFromThermalStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~CheckUseTempFromThermalStudy.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

This property is valid only if:

- [ICWNonLinearStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.
- [ICWNonLinearStudyOptions::ThermalStudyName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalStudyName.html) is specified and is a transient thermal study.

If this property is set to 0, use [ICWNonLinearStudyOptions::TimeStep](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeStep.html) to specify the time step at which to import a single temperature from a transient thermal study.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
