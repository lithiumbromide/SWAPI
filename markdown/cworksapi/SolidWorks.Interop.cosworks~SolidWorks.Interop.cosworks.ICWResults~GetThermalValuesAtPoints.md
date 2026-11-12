---
title: "GetThermalValuesAtPoints Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetThermalValuesAtPoints"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalValuesAtPoints.html"
---

# GetThermalValuesAtPoints Method (ICWResults)

Gets thermal values at the specified solution step and the specified points.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThermalValuesAtPoints( _
   ByVal NComponent As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArrayPoints As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim ArrayPoints As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetThermalValuesAtPoints(NComponent, NStepNumber, DispPlane, ArrayPoints, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetThermalValuesAtPoints(
   System.int NComponent,
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArrayPoints,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetThermalValuesAtPoints(
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArrayPoints,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Thermal component as defined in [swsThermalComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsThermalComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for steady state)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArrayPoints`: Array of point coordinates
- `NUnits`: Temperature unit as defined [swsTemperatureUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of NComponent results for ArrayPoints at NStepNumber

## VBA Syntax

See [CWResults::GetThermalValuesAtPoints](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetThermalValuesAtPoints.html).

## Examples

[Get Thermal Values (VBA)](Get_Thermal_Values_at_Points_Example_VB.htm)
[Get Thermal Values (VB.NET)](Get_Thermal_Values_at_Points_Example_VBNET.htm)
[Get Thermal Values (C#)](Get_Thermal_Values_at_Points_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetThermalValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalValues.html)
[ICWResults::GetMinMaxThermal Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxThermal.html)
[ICWResults::GetThermalComponentForAllStepsAtNode Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalComponentForAllStepsAtNode.html)
[ICWResults::GetThermalForEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetThermalForEntities.html)
[ICWResults::GetHeatPowerOrEnergy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetHeatPowerOrEnergy.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
