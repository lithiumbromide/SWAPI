---
title: "IncludeThermostat Property (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "IncludeThermostat"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~IncludeThermostat.html"
---

# IncludeThermostat Property (ICWHeatFlux)

Obsolete. Superseded by [ICWHeatFlux::IncludeThermostat2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~IncludeThermostat2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeThermostat As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Integer

instance.IncludeThermostat = value

value = instance.IncludeThermostat
```

### C#

```csharp
System.int IncludeThermostat {get; set;}
```

### C++/CLI

```cpp
property System.int IncludeThermostat {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to include thermostat effects, 0 to not

## VBA Syntax

See [CWHeatFlux::IncludeThermostat](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~IncludeThermostat.html).

## Remarks

Thermostat is used for transient thermal studies only.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::GetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetThermostat.html)
[ICWHeatFlux::SetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetThermostat.html)
[ICWHeatFlux::ThermostatUnits Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~ThermostatUnits.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
