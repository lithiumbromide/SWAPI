---
title: "ThermalStudyNameUsedForInitialTemperature Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "ThermalStudyNameUsedForInitialTemperature"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~ThermalStudyNameUsedForInitialTemperature.html"
---

# ThermalStudyNameUsedForInitialTemperature Property (ICWThermalStudyOptions)

Gets or sets the thermal study name for initial temperature from the thermal study. Used for thermal transient studies only.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalStudyNameUsedForInitialTemperature As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
Dim value As System.String

instance.ThermalStudyNameUsedForInitialTemperature = value

value = instance.ThermalStudyNameUsedForInitialTemperature
```

### C#

```csharp
System.string ThermalStudyNameUsedForInitialTemperature {get; set;}
```

### C++/CLI

```cpp
property System.String^ ThermalStudyNameUsedForInitialTemperature {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Thermal study name

## VBA Syntax

See [CWThermalStudyOptions::ThermalStudyNameUsedForInitialTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~ThermalStudyNameUsedForInitialTemperature.html).

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
