---
title: "GetThermalValues Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetThermalValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalValues.html"
---

# GetThermalValues Method (ICWResults)

Gets thermal values for all nodes at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThermalValues( _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetThermalValues(NStepNumber, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetThermalValues(
   System.int NStepNumber,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetThermalValues(
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NStepNumber`: Solution step number (use 1 for steady state)
- `DispPlane`: Reference geometry
- `NUnits`: Temperature unit as defined [swsTemperatureUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of thermal results (see **Remarks**)

## VBA Syntax

See [CWResults::GetThermalValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetThermalValues.html).

## Examples

[Get Thermal Values (VBA)](Get_Thermal_Values_at_Points_Example_VB.htm)
[Get Thermal Values (VB.NET)](Get_Thermal_Values_at_Points_Example_VBNET.htm)
[Get Thermal Values (C#)](Get_Thermal_Values_at_Points_Example_CSharp.htm)

## Remarks

This method returns the following array:

{

node`_1`, `temp_1, gradx_1, grady_1, gradz_1, gradn_1, hfluxx_1, hfluxy_1, hfluxz_1, hfluxn_1,`

`node_2`, `temp_2`, `gradx_2, grady_2, gradz_2, gradn_2, hfluxx_1, hfluxy_1, hfluxz_1, hfluxn_1,`

node`_3`, `temp_3`, `gradx_3, grady_3, gradz_3, gradn_3, hfluxx_1, hfluxy_1, hfluxz_1, hfluxn_1,`

...,

node`_n`, `temp_n, gradx_n, grady_n, gradz_n, gradn_n, hfluxx_1, hfluxy_1, hfluxz_1, hfluxn_1`

},

where the nodes are integers, and the temperatures, temperature gradients, and heat fluxes are doubles.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxThermal Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxThermal.html)
[ICWResults::GetThermalComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalComponentForAllStepsAtNode.html)
[ICWResults::GetThermalForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalForEntities.html)
[ICWResults::GetThermalValuesAtPoints Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalValuesAtPoints.html)
[ICWResults::GetHeatPowerOrEnergy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetHeatPowerOrEnergy.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
