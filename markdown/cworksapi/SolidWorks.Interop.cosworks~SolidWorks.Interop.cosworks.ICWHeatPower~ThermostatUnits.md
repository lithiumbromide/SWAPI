---
title: "ThermostatUnits Property (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "ThermostatUnits"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~ThermostatUnits.html"
---

# ThermostatUnits Property (ICWHeatPower)

Gets or sets the thermostat units for heat power.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermostatUnits As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim value As System.Integer

instance.ThermostatUnits = value

value = instance.ThermostatUnits
```

### C#

```csharp
System.int ThermostatUnits {get; set;}
```

### C++/CLI

```cpp
property System.int ThermostatUnits {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Temperature unit as defined [swsTemperatureUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureUnit_e.html)

## VBA Syntax

See [CWHeatPower::ThermostatUnits](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~ThermostatUnits.html).

## Examples

See the [ICWHeatPower](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html) examples.

## Remarks

Thermostat is used for transient thermal studies only.

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::GetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetThermostat.html)
[ICWHeatPower::SetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetThermostat.html)
[ICWHeatPower::IncludeThermostat Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~IncludeThermostat.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
