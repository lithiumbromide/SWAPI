---
title: "GetThermostat Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "GetThermostat"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetThermostat.html"
---

# GetThermostat Method (ICWHeatFlux)

Gets the location of the thermostat for heat flux.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThermostat() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Object

value = instance.GetThermostat()
```

### C#

```csharp
System.object GetThermostat()
```

### C++/CLI

```cpp
System.Object^ GetThermostat();
```

### Return Value

Vertex of the location of the thermostat

## VBA Syntax

See [CWHeatFlux::GetThermostat](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~GetThermostat.html).

## Remarks

Thermostat is used for transient thermal studies only.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::SetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetThermostat.html)
[ICWHeatFlux::IncludeThermostat Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~IncludeThermostat.html)
[ICWHeatFlux::ThermostatUnits Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~ThermostatUnits.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
