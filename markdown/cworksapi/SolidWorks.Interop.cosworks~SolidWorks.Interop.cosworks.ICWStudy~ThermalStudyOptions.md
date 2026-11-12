---
title: "ThermalStudyOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "ThermalStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ThermalStudyOptions.html"
---

# ThermalStudyOptions Property (ICWStudy)

Gets the options for this thermal study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ThermalStudyOptions As CWThermalStudyOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWThermalStudyOptions

value = instance.ThermalStudyOptions
```

### C#

```csharp
CWThermalStudyOptions ThermalStudyOptions {get;}
```

### C++/CLI

```cpp
property CWThermalStudyOptions^ ThermalStudyOptions {
   CWThermalStudyOptions^ get();
}
```

### Property Value

[Thermal study options](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html)

## VBA Syntax

See [CWStudy::ThermalStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~ThermalStudyOptions.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
