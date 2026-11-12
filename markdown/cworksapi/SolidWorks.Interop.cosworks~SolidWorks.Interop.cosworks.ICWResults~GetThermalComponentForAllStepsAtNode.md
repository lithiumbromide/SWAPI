---
title: "GetThermalComponentForAllStepsAtNode Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetThermalComponentForAllStepsAtNode"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalComponentForAllStepsAtNode.html"
---

# GetThermalComponentForAllStepsAtNode Method (ICWResults)

Gets thermal values at the specified node for all solutions steps.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThermalComponentForAllStepsAtNode( _
   ByVal NComponent As System.Integer, _
   ByVal NNodeNum As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NNodeNum As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetThermalComponentForAllStepsAtNode(NComponent, NNodeNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetThermalComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetThermalComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Thermal component as defined in [swsThermalComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsThermalComponent_e.html)
- `NNodeNum`: Node number
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is a scalar component and not a directional component
- `NUnits`: Temperature unit as defined [swsTemperatureUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of thermal results (see **Remarks**)

## VBA Syntax

See [CWResults::GetThermalComponentForAllStepsAtNode](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetThermalComponentForAllStepsAtNode.html).

## Examples

[Get Thermal Values (VBA)](Get_Thermal_Values_at_Points_Example_VB.htm)
[Get Thermal Values (VB.NET)](Get_Thermal_Values_at_Points_Example_VBNET.htm)
[Get Thermal Values (C#)](Get_Thermal_Values_at_Points_Example_CSharp.htm)

## Remarks

This method returns the following array:

{

`solution_step_1`, `time_1`, `temp_1,`

`solution_step_2`, `time_2`, `temp_2,`

`solution_step_3`, `time_3`, `temp_3,`

...,

`solution_step_n`, `time_n`, `temp_n`

},

where the solution steps are integers, `time_n` = (`solution_step_n` * 60) seconds, and the temperatures are doubles.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxThermal Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxThermal.html)
[ICWResults::GetThermalForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalForEntities.html)
[ICWResults::GetThermalValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalValues.html)
[ICWResults::GetThermalValuesAtPoints Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalValuesAtPoints.html)
[ICWResults::GetHeatPowerOrEnergy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetHeatPowerOrEnergy.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
