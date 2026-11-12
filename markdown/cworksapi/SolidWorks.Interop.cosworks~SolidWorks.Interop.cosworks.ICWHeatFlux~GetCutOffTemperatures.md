---
title: "GetCutOffTemperatures Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "GetCutOffTemperatures"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetCutOffTemperatures.html"
---

# GetCutOffTemperatures Method (ICWHeatFlux)

Gets the thermostat lower- and upper-bound temperatures in this heat flux load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetCutOffTemperatures( _
   ByRef DVal1 As System.Double, _
   ByRef DVal2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim DVal1 As System.Double
Dim DVal2 As System.Double

instance.GetCutOffTemperatures(DVal1, DVal2)
```

### C#

```csharp
void GetCutOffTemperatures(
   out System.double DVal1,
   out System.double DVal2
)
```

### C++/CLI

```cpp
void GetCutOffTemperatures(
   [Out] System.double DVal1,
   [Out] System.double DVal2
)
```

### Parameters

- `DVal1`: Lower-bound temperature
- `DVal2`: Upper-bound temperature

## VBA Syntax

See [CWHeatFlux::GetCutOffTemperatures](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~GetCutOffTemperatures.html).

## Examples

See the [ICWHeatFlux](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html) examples.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::SetCutOffTemperatures Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetCutOffTemperatures.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
