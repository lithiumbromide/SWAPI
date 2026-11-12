---
title: "ThermostatUnits Property (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "ThermostatUnits"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~ThermostatUnits.html"
---

# ThermostatUnits Property (ICWHeatFlux)

Gets or sets the thermostat units for heat flux.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermostatUnits As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
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

See [CWHeatFlux::ThermostatUnits](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~ThermostatUnits.html).

## Examples

See the [ICWHeatFlux](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html) examples.

## Remarks

Thermostat is used for transient thermal studies only.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::IncludeThermostat Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~IncludeThermostat.html)
[ICWHeatFlux::GetThermostat Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetThermostat.html)
[ICWHeatFlux::SetThermostat Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetThermostat.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
