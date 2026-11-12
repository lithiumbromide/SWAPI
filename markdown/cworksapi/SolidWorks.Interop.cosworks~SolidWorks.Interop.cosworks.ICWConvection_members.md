---
title: "ICWConvection Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html"
---

# ICWConvection Interface Members

The following tables list the members exposed by [ICWConvection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BulkAmbientTemperature | Gets or sets the bulk ambient temperature for defining convection for thermal studies. |
| Property | ConvectionCoefficient | Gets or sets the convection coefficient used in defining convection for thermal studies. |
| Property | Unit | Gets or sets the units for convection. |
| Property | UseBulkTemperatureTimeCurve | Obsolete. Superseded by ICWConvection::UseBulkTemperatureTimeCurve2 . |
| Property | UseBulkTemperatureTimeCurve2 | Gets or sets whether to use a bulk temperature curve for convection. |
| Property | UseTemperatureCurve | Obsolete. Superseded by ICWConvection::UseTemperatureCurve2 . |
| Property | UseTemperatureCurve2 | Gets or sets whether to use a temperature curve for convection. |
| Property | UseTimeCurve | Obsolete. Superseded by ICWConvection::UseTimeCurve2 . |
| Property | UseTimeCurve2 | Gets or sets whether to use a time curve for convection. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ConvectionBeginEdit | Starts editing convection. |
| Method | ConvectionEndEdit | Ends the editing convection. |
| Method | GetBulkTemperatureTimeCurve | Gets the bulk temperature versus time curve data for convection. |
| Method | GetTemperatureCurve | Gets the temperature curve data for convection. |
| Method | GetTimeCurve | Gets the time curve data for convection. |
| Method | InsertEntity | Inserts an entity for applying convection. |
| Method | RemoveEntity | Removes the entity at the specified index to which to apply convection. |
| Method | SetBulkTemperatureTimeCurve | Obsolete. Superseded by ICWConvection::SetBulkTemperatureTimeCurve2 . |
| Method | SetBulkTemperatureTimeCurve2 | Sets the bulk temperature-time curve data. |
| Method | SetTemperatureCurve | Obsolete. Superseded by ICWConvection::SetTemperatureCurve2 . |
| Method | SetTemperatureCurve2 | Sets the temperature curve data for convection. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWConvection::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Sets the time curve data for convection. |

[Top](#topBookmark)

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
