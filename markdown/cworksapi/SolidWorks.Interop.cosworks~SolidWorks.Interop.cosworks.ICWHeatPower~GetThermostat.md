---
title: "GetThermostat Method (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "GetThermostat"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetThermostat.html"
---

# GetThermostat Method (ICWHeatPower)

Gets the location of the thermostat for heat power.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThermostat() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
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

Vertex for the location of heat power

## VBA Syntax

See [CWHeatPower::GetThermostat](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~GetThermostat.html).

## Remarks

Thermostat is used for transient thermal studies only.

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::SetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetThermostat.html)
[ICWHeatPower::IncludeThermostat Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~IncludeThermostat.html)
[ICWHeatPower::ThermostatUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~ThermostatUnits.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
