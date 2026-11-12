---
title: "ICWHeatPower Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html"
---

# ICWHeatPower Interface Members

The following tables list the members exposed by [ICWHeatPower](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | HPValue | Gets or sets the heat power value for heat power. |
| Property | IncludeThermostat | Obsolete. Superseded by ICWHeatPower::IncludeThermostat2 . |
| Property | IncludeThermostat2 | Gets or sets whether to include thermostat effects in heat power for transient thermal studies. |
| Property | ReverseDirection | Obsolete. Superseded by ICWHeatPower::ReverseDirection2 . |
| Property | ReverseDirection2 | Gets or sets whether to reverse the direction of heat power. |
| Property | ThermostatUnits | Gets or sets the thermostat units for heat power. |
| Property | Unit | Gets or sets the units of heat power. |
| Property | UseTemperatureCurve | Obsolete. Superseded by ICWHeatPower::UseTemperatureCurve2 . |
| Property | UseTemperatureCurve2 | Gets or sets whether to use a temperature curve for heat power. |
| Property | UseTimeCurve | Obsolete. Superseded by ICWHeatPower::UseTimeCurve2 . |
| Property | UseTimeCurve2 | Gets or sets whether to use a time curve for heat power. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetCutOffTemperatures | Gets the thermostat cut off temperatures (lower and upper bounds) used in heat power for transient thermal studies. |
| Method | GetTemperatureCurve | Gets the temperature curve data for heat power. |
| Method | GetThermostat | Gets the location of the thermostat for heat power. |
| Method | GetTimeCurve | Gets the time curve data for heat power. |
| Method | HeatPowerBeginEdit | Starts editing heat power. |
| Method | HeatPowerEndEdit | Ends editing heat power. |
| Method | InsertEntity | Inserts a new entity for heat power. |
| Method | RemoveEntity | Removes the entity at the specified index to which to apply heat power. |
| Method | SetCutOffTemperatures | Sets the thermostat cut off temperatures (lower and upper bounds) used in heat power for transient thermal studies. |
| Method | SetTemperatureCurve | Obsolete. Superseded by ICWHeatPower::SetTemperatureCurve2 . |
| Method | SetTemperatureCurve2 | Sets the temperature curve data for heat power. |
| Method | SetThermostat | Sets a vertex for the location of a thermostat for heat power. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWHeatPower::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Sets the time curve data for heat power. |

[Top](#topBookmark)

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
