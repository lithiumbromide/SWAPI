---
title: "ICWRadiation Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html"
---

# ICWRadiation Interface Members

The following tables list the members exposed by [ICWRadiation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AmbientTemperature | Gets or sets the value of ambient temperature for this radiation. |
| Property | Emmisivity | Gets or sets the value for emissivity for this radiation. |
| Property | OpenSystem | Obsolete. Superseded by ICWRadiation::OpenSystem2 . |
| Property | OpenSystem2 | Gets or sets whether to consider radiation to the ambient (open system). |
| Property | RadiationType | Gets or sets the type of radiation. |
| Property | Unit | Gets or sets the units of radiation. |
| Property | UseTemperatureCurve | Obsolete. Superseded by ICWRadiation::UseTemperatureCurve2 . |
| Property | UseTemperatureCurve2 | Gets or sets whether to use a temperature curve for this radiation. |
| Property | UseTimeCurve | Obsolete. Superseded by ICWRadiation::UseTimeCurve2 . |
| Property | UseTimeCurve2 | Gets or sets whether to use a time curve for this radiation. |
| Property | ViewFactor | Gets or sets the value of the view factor for this radiation. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetTemperatureCurve | Gets the temperature curve data for this radiation. |
| Method | GetTimeCurve | Gets the time curve data for this radiation. |
| Method | InsertEntity | Inserts a new entity for radiation. |
| Method | RadiationBeginEdit | Starts editing radiation. |
| Method | RadiationEndEdit | Ends editing radiation. |
| Method | RemoveEntity | Removes the entity at the specified index from this radiation. |
| Method | SetTemperatureCurve | Obsolete. Superseded by ICWRadiation::SetTemperatureCurve2 . |
| Method | SetTemperatureCurve2 | Sets the temperature curve data for this radiation. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWRadiation::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Sets the time curve data for this radiation. |

[Top](#topBookmark)

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
