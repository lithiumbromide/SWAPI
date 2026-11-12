---
title: "SetCutOffTemperatures Method (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "SetCutOffTemperatures"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetCutOffTemperatures.html"
---

# SetCutOffTemperatures Method (ICWHeatPower)

Sets the thermostat cut off temperatures (lower and upper bounds) used in heat power for transient thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCutOffTemperatures( _
   ByVal DVal1 As System.Double, _
   ByVal DVal2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim DVal1 As System.Double
Dim DVal2 As System.Double

instance.SetCutOffTemperatures(DVal1, DVal2)
```

### C#

```csharp
void SetCutOffTemperatures(
   System.double DVal1,
   System.double DVal2
)
```

### C++/CLI

```cpp
void SetCutOffTemperatures(
   System.double DVal1,
   System.double DVal2
)
```

### Parameters

- `DVal1`: Lower-bound temperature
- `DVal2`: Upper-bound temperature

## VBA Syntax

See [CWHeatPower::SetCutOffTemperatures](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~SetCutOffTemperatures.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::GetCutOffTemperatures Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetCutOffTemperatures.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
