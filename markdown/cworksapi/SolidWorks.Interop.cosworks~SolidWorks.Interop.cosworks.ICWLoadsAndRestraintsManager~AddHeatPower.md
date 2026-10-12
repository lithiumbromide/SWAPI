---
title: "AddHeatPower Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddHeatPower"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddHeatPower.html"
---

# AddHeatPower Method (ICWLoadsAndRestraintsManager)

Creates a heat power load for thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddHeatPower( _
   ByVal DispArray As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWHeatPower
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispArray As System.Object
Dim ErrorCode As System.Integer
Dim value As CWHeatPower

value = instance.AddHeatPower(DispArray, ErrorCode)
```

### C#

```csharp
CWHeatPower AddHeatPower(
   System.object DispArray,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWHeatPower^ AddHeatPower(
   System.Object^ DispArray,
   [Out] System.int ErrorCode
)
```

### Parameters

- `DispArray`: Array of entities (bodies, faces, edges, and vertices) to which to apply heat power
- `ErrorCode`: Error as defined in [swsHeatPowerError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsHeatPowerError_e.html)

### Return Value

[Heat power](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWHeatPower.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddHeatPower](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddHeatPower.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## Remarks

The specified value is applied to each entity.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
