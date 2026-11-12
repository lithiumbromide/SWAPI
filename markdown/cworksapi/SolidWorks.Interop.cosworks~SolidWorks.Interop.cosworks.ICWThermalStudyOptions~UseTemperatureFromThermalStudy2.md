---
title: "UseTemperatureFromThermalStudy2 Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "UseTemperatureFromThermalStudy2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~UseTemperatureFromThermalStudy2.html"
---

# UseTemperatureFromThermalStudy2 Property (ICWThermalStudyOptions)

Gets or sets the status of initial temperature from the thermal study.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTemperatureFromThermalStudy2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.Boolean

instance.UseTemperatureFromThermalStudy2 = value

value = instance.UseTemperatureFromThermalStudy2
```

### C#

```csharp
System.bool UseTemperatureFromThermalStudy2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseTemperatureFromThermalStudy2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Use initial temperature from the thermal study
- 0 or false = Do not use initial temperature from the thermal study

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
