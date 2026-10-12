---
title: "GetHeatPowerOrEnergy2 Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetHeatPowerOrEnergy2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetHeatPowerOrEnergy2.html"
---

# GetHeatPowerOrEnergy2 Method (ICWResults)

Gets the heat power or heat energy for the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHeatPowerOrEnergy2( _
   ByVal BHeatEnergy As System.Boolean, _
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
Dim BHeatEnergy As System.Boolean
Dim ArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim NStepNumber As System.Integer
Dim NStepNumber2 As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetHeatPowerOrEnergy2(BHeatEnergy, ArraySelectedEntities, NUnits, NStepNumber, NStepNumber2, ErrorCode)
```

### C#

```csharp
System.object GetHeatPowerOrEnergy2(
   System.bool BHeatEnergy,
   System.object ArraySelectedEntities,
   System.int NUnits,
   System.int NStepNumber,
   System.int NStepNumber2,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetHeatPowerOrEnergy2(
   System.bool BHeatEnergy,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   System.int NStepNumber,
   System.int NStepNumber2,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BHeatEnergy`: 0 or false for heat power, -1 or true for heat energy
- `ArraySelectedEntities`: Array of geometric entities
- `NUnits`: Units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `NStepNumber`: Solution step number (use 1 for steady state)
- `NStepNumber2`: End solution step number (use 1 for steady state); valid only if BHeatEnergy is 1
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of heat values (see **Remarks**)

## Examples

[Get Thermal Values (VBA)](Get_Thermal_Values_at_Points_Example_VB.htm)
[Get Thermal Values (VB.NET)](Get_Thermal_Values_at_Points_Example_VBNET.htm)
[Get Thermal Values (C#)](Get_Thermal_Values_at_Points_Example_CSharp.htm)

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

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
