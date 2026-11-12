---
title: "SetThermostat Method (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "SetThermostat"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetThermostat.html"
---

# SetThermostat Method (ICWHeatPower)

Sets a vertex for the location of a thermostat for heat power.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetThermostat( _
   ByVal DispVertex As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim DispVertex As System.Object

instance.SetThermostat(DispVertex)
```

### C#

```csharp
void SetThermostat(
   System.object DispVertex
)
```

### C++/CLI

```cpp
void SetThermostat(
   System.Object^ DispVertex
)
```

### Parameters

- `DispVertex`: Vertex for the location of a thermostat

## VBA Syntax

See [CWHeatPower::SetThermostat](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~SetThermostat.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## Remarks

Thermostat is used for transient thermal studies only.

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::GetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetThermostat.html)
[ICWHeatPower::IncludeThermostat Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~IncludeThermostat.html)
[ICWHeatPower::ThermostatUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~ThermostatUnits.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
