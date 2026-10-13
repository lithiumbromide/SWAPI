---
title: "ICWTemperature Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTemperature_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature_members.html"
---

# ICWTemperature Interface Members

The following tables list the members exposed by [ICWTemperature](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | TemperatureType | Gets or sets the temperature type for transient studies. |
| Property | TemperatureValue | Gets or sets the temperature. |
| Property | Unit | Gets or sets the units of temperature. |
| Property | UseTimeCurve | Obsolete. Superseded by ICWTemperature::UseTimeCurve2 . |
| Property | UseTimeCurve2 | Gets or sets whether to use time curve data with the temperature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetTimeCurve | Gets the time curve data for the temperature. |
| Method | InsertEntity | Inserts a new entity for the temperature. |
| Method | RemoveEntity | Removes the entity at the specified index to which to apply the temperature. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWTemperature::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Sets the time curve data. |
| Method | TemperatureBeginEdit | Starts editing the temperature. |
| Method | TemperatureEndEdit | Ends editing the temperature. |

[Top](#topBookmark)

## See Also

[ICWTemperature Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
