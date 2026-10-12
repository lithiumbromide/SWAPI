---
title: "GetHeatPowerOrEnergy Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetHeatPowerOrEnergy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetHeatPowerOrEnergy.html"
---

# GetHeatPowerOrEnergy Method (ICWResults)

Obsolete. Superseded by [ICWResults::GetHeatPowerOrEnergy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetHeatPowerOrEnergy2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHeatPowerOrEnergy( _
   ByVal BHeatEnergy As System.Integer, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal NStepNumber2 As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim BHeatEnergy As System.Integer
Dim ArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim NStepNumber As System.Integer
Dim NStepNumber2 As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetHeatPowerOrEnergy(BHeatEnergy, ArraySelectedEntities, NUnits, NStepNumber, NStepNumber2, ErrorCode)
```

### C#

```csharp
System.object GetHeatPowerOrEnergy(
   System.int BHeatEnergy,
   System.object ArraySelectedEntities,
   System.int NUnits,
   System.int NStepNumber,
   System.int NStepNumber2,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetHeatPowerOrEnergy(
   System.int BHeatEnergy,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   System.int NStepNumber,
   System.int NStepNumber2,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BHeatEnergy`: 0 for heat power, 1 for heat energy
- `ArraySelectedEntities`: Array of geometric entities
- `NUnits`: Units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `NStepNumber`: Solution step number (use 1 for steady state)
- `NStepNumber2`: End solution step number (use 1 for steady state); valid only if BHeatEnergy is 1
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of heat values (see **Remarks**)

## VBA Syntax

See [CWResults::GetHeatPowerOrEnergy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetHeatPowerOrEnergy.html).

## Remarks

This method returns the following array:

{

`sel_power_or_energy_in`,

`sel_power_or_energy_out`,

`sel_net_power`,

`model_power_or_energy_in`,

`model_power_or_energy_out`,

`model_net_power_or_energy`

},

where `sel_power_or_energy_in` and `sel_power_or_energy_out` are the sum of individual entity in and out values, and `model_power_or_energy_in` and `model_power_or_energy_out` are total in and out values for the entire model.

`sel_net_power` = (`sel_power_or_energy_in` - `sel_power_or_energy_out)`

`model_net_power_or_energy` = (`model_power_or_energy_in` - `model_power_or_energy_out)`

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxThermal Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxThermal.html)
[ICWResults::GetThermalComponentForAllStepsAtNode Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalComponentForAllStepsAtNode.html)
[ICWResults::GetThermalForEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalForEntities.html)
[ICWResults::GetThermalValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalValues.html)
[ICWResults::GetThermalValuesAtPoints Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalValuesAtPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
