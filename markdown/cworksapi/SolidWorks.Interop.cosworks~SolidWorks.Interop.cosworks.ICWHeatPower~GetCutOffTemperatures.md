---
title: "GetCutOffTemperatures Method (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "GetCutOffTemperatures"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetCutOffTemperatures.html"
---

# GetCutOffTemperatures Method (ICWHeatPower)

Gets the thermostat cut off temperatures (lower and upper bounds) used in heat power for transient thermal studies.

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
Dim instance As ICWHeatPower
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
- `DVal2`: Lower-bound temperature

## VBA Syntax

See [CWHeatPower::GetCutOffTemperatures](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~GetCutOffTemperatures.html).

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::SetCutOffTemperatures Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetCutOffTemperatures.html)
[ICWHeatPower::UseTemperatureCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~UseTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
