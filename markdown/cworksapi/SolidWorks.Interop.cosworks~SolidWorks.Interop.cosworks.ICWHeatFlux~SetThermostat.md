---
title: "SetThermostat Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "SetThermostat"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetThermostat.html"
---

# SetThermostat Method (ICWHeatFlux)

Sets the location of the thermostat for heat flux used in transient thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetThermostat( _
   ByVal DispCoord As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim DispCoord As System.Object

instance.SetThermostat(DispCoord)
```

### C#

```csharp
void SetThermostat(
   System.object DispCoord
)
```

### C++/CLI

```cpp
void SetThermostat(
   System.Object^ DispCoord
)
```

### Parameters

- `DispCoord`: Vertex of the location of the thermostat

## VBA Syntax

See [CWHeatFlux::SetThermostat](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~SetThermostat.html).

## Examples

See the [ICWHeatFlux](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html) examples.

## Remarks

Thermostat is used for transient thermal studies only.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::GetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetThermostat.html)
[ICWHeatFlux::IncludeThermostat Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~IncludeThermostat.html)
[ICWHeatFlux::ThermostatUnits Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~ThermostatUnits.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
