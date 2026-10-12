---
title: "CheckUseTempFromThermalStudy2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "CheckUseTempFromThermalStudy2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckUseTempFromThermalStudy2.html"
---

# CheckUseTempFromThermalStudy2 Property (ICWNonLinearStudyOptions)

Gets or sets whether to use the temperature from the corresponding time of a transient thermal analysis at each nonlinear time step.

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckUseTempFromThermalStudy2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Boolean

instance.CheckUseTempFromThermalStudy2 = value

value = instance.CheckUseTempFromThermalStudy2
```

### C#

```csharp
System.bool CheckUseTempFromThermalStudy2 {get; set;}
```

### C++/CLI

```cpp
property System.bool CheckUseTempFromThermalStudy2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to use the temperature from the corresponding time of a transient thermal analysis at each nonlinear time step, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::CheckUseTempFromThermalStudy2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~CheckUseTempFromThermalStudy2.html).

## Remarks

This property is valid only if:

- [ICWNonLinearStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromThermalStudy.
- [ICWNonLinearStudyOptions::ThermalStudyName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalStudyName.html) is specified and is a transient thermal study.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is set to false or 0, use [ICWNonLinearStudyOptions::TimeStep](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeStep.html) to specify the time step at which to import a single temperature from a transient thermal study.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
