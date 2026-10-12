---
title: "UseTemperatureFromThermalStudy Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "UseTemperatureFromThermalStudy"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~UseTemperatureFromThermalStudy.html"
---

# UseTemperatureFromThermalStudy Property (ICWThermalStudyOptions)

Obsolete. Superseded by [ICWThermalStudyOptions::UseTemperatureFromThermalStudy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~UseTemperatureFromThermalStudy2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTemperatureFromThermalStudy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Integer

instance.UseTemperatureFromThermalStudy = value

value = instance.UseTemperatureFromThermalStudy
```

### C#

```csharp
System.int UseTemperatureFromThermalStudy {get; set;}
```

### C++/CLI

```cpp
property System.int UseTemperatureFromThermalStudy {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use initial temperature from the thermal study
- 0 = Do not use initial temperature from the thermal study

## VBA Syntax

See [CWThermalStudyOptions::UseTemperatureFromThermalStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~UseTemperatureFromThermalStudy.html).

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
