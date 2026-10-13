---
title: "IncludeThermostat Property (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "IncludeThermostat"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~IncludeThermostat.html"
---

# IncludeThermostat Property (ICWHeatPower)

Obsolete. Superseded by [ICWHeatPower::IncludeThermostat2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~IncludeThermostat2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeThermostat As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
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

1 to include thermostat, 0 to not

## VBA Syntax

See [CWHeatPower::IncludeThermostat](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~IncludeThermostat.html).

## Remarks

Thermostat is used for transient [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies only.

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::GetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetThermostat.html)
[ICWHeatPower::SetThermostat Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetThermostat.html)
[ICWHeatPower::ThermostatUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~ThermostatUnits.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
