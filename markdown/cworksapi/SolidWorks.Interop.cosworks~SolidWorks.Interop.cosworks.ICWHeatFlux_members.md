---
title: "ICWHeatFlux Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html"
---

# ICWHeatFlux Interface Members

The following tables list the members exposed by [ICWHeatFlux](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | HFValue | Gets or sets the heat flux value used in thermal studies. |
| Property | IncludeThermostat | Obsolete. Superseded by ICWHeatFlux::IncludeThermostat2 . |
| Property | IncludeThermostat2 | Gets or sets whether to include thermostat effects in this heat flux. |
| Property | PerUnitLength | Obsolete. Superseded by ICWHeatFlux::PerUnitLength2 . |
| Property | PerUnitLength2 | Gets or sets whether heat flux uses per unit length while selecting beam bodies. |
| Property | ReverseDirection | Obsolete. Superseded by ICWHeatFlux::ReverseDirection2 . |
| Property | ReverseDirection2 | Gets or sets whether to reverse the direction of heat flux. |
| Property | ThermostatUnits | Gets or sets the thermostat units for heat flux. |
| Property | Unit | Gets or sets the temperature unit to use with this heat flux. |
| Property | UseTemperatureCurve | Obsolete. Superseded by ICWHeatFlux::UseTemperatureCurve2 . |
| Property | UseTemperatureCurve2 | Gets or sets whether to use a temperature curve for this heat flux. |
| Property | UseTimeCurve | Obsolete. Superseded by ICWHeatFlux::UseTimeCurve2 . |
| Property | UseTimeCurve2 | Gets or sets whether to use a time curve for this heat flux. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetCutOffTemperatures | Gets the thermostat lower- and upper-bound temperatures in this heat flux load. |
| Method | GetTemperatureCurve | Gets the temperature curve data for heat flux. |
| Method | GetThermostat | Gets the location of the thermostat for heat flux. |
| Method | GetTimeCurve | Gets the time curve data for heat flux. |
| Method | HeatFluxBeginEdit | Starts editing heat flux. |
| Method | HeatFluxEndEdit | Ends editing heat flux. |
| Method | InsertEntity | Inserts an entity on which to apply this heat flux. |
| Method | RemoveEntity | Removes an entity from this heat flux. |
| Method | SetCutOffTemperatures | Sets the thermostat lower- and upper-bound temperatures for this heat flux. |
| Method | SetTemperatureCurve | Obsolete. Superseded by ICWHeatFlux::SetTemperatureCurve2 . |
| Method | SetTemperatureCurve2 | Sets the temperature curve data for heat flux. |
| Method | SetThermostat | Sets the location of the thermostat for heat flux used in transient thermal studies. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWHeatFlux::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Sets the time curve data for heat flux. |

[Top](#topBookmark)

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
