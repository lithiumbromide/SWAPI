---
title: "SetCutOffTemperatures Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "SetCutOffTemperatures"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetCutOffTemperatures.html"
---

# SetCutOffTemperatures Method (ICWHeatFlux)

Sets the thermostat lower- and upper-bound temperatures for this heat flux.

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
Dim instance As ICWHeatFlux
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

See [CWHeatFlux::SetCutOffTemperatures](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~SetCutOffTemperatures.html).

## Remarks

Thermostat is used for transient thermal studies only.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::GetCutOffTemperatures Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetCutOffTemperatures.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
