---
title: "ICWBearingLoad Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html"
---

# ICWBearingLoad Interface Members

The following tables list the members exposed by [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BearingLoadUnit | Gets or sets the unit system for this bearing load. |
| Property | Direction | Gets or sets the direction of this bearing load in the selected coordinate system. |
| Property | DistributionType | Gets or sets the distribution type of this bearing load. |
| Property | UseTimeCurve | Obsolete. Superseded by ICWBearingLoad::UseTimeCurve2 . |
| Property | UseTimeCurve2 | Gets or sets whether to use a time curve for this bearing load. |
| Property | XDirectionReverse | Obsolete. Superseded by ICWBearingLoad::XDirectionReverse2 . |
| Property | XDirectionReverse2 | Gets or sets whether to reverse the X direction of this bearing load. |
| Property | XDirectionValue | Gets or sets the value of the bearing load in the X direction of the selected coordinate system. |
| Property | YDirectionReverse | Obsolete. Superseded by ICWBearingLoad::YDirectionReverse2 . |
| Property | YDirectionReverse2 | Gets or sets whether to reverse the Y direction of this bearing load. |
| Property | YDirectionValue | Gets or sets the value of the bearing load in the Y direction of the selected coordinate system. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | BearingLoadBeginEdit | Starts editing a bearing load. |
| Method | BearingLoadEndEdit | Ends editing a bearing load. |
| Method | GetEntityCount | Gets the number of entities for the bearing load. |
| Method | GetTimeCurve | Gets the time curve data for the bearing load of this dynamic study. |
| Method | InsertEntity | Inserts a source entity for the bearing load. |
| Method | RemoveEntity | Removes a source entity at the specified index from the bearing load. |
| Method | ReplaceCoordinateSystem | Replace the current coordinate system with the specified coordinate system. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWBearingLoad::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Defines a time curve for the bearing load of this dynamic study. |

[Top](#topBookmark)

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
