---
title: "AddTemperature Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddTemperature"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddTemperature.html"
---

# AddTemperature Method (ICWLoadsAndRestraintsManager)

Creates a temperature load for thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddTemperature( _
   ByVal DispArray As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWTemperature
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispArray As System.Object
Dim ErrorCode As System.Integer
Dim value As CWTemperature

value = instance.AddTemperature(DispArray, ErrorCode)
```

### C#

```csharp
CWTemperature AddTemperature(
   System.object DispArray,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTemperature^ AddTemperature(
   System.Object^ DispArray,
   [Out] System.int ErrorCode
)
```

### Parameters

- `DispArray`: Array of entities (faces, edges, and vertices) to which to apply temperature
- `ErrorCode`: Error as defined in [swsTemperatureError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureError_e.html)

### Return Value

[Temperature](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWTemperature.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddTemperature.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## Remarks

Temperature can be used with static, nonlinear, frequency, buckling, and thermal studies.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simuluation API 2008 SP1.0
