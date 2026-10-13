---
title: "IHelixFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html"
---

# IHelixFeatureData Interface Members

The following tables list the members exposed by [IHelixFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Clockwise | Gets or sets the direction of the turns of this helix feature. |
| Property | DefinedBy | Gets or sets the definition of this helix feature. |
| Property | Height | Gets or sets the height of this helix feature. |
| Property | Pitch | Gets or sets the pitch of this helix feature. |
| Property | PitchCount | Gets the number of regions in this variable-pitch helix. |
| Property | ReverseDirection | Gets or sets whether to make this helix feature extend backward from the point of origin. |
| Property | Revolution | Gets or sets the number of revolutions for this helix feature. |
| Property | StartingAngle | Gets or sets the angle for the first turn of this helix feature. |
| Property | Taper | Gets or sets whether this constant-pitch helix feature is tapered. |
| Property | TaperAngle | Gets or sets the angle of the taper for this constant-pitch helix feature. |
| Property | TaperOutward | Gets or sets the direction of the taper for this constant-pitch helix feature. |
| Property | VariablePitch | Gets whether this helix feature has a variable or constant pitch. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddLastRecord | Adds a region to the end of the Region parameters table of this variable-pitch helix. |
| Method | DeleteRecord | Deletes the specified records in the Region parameters table of this variable-pitch helix. |
| Method | GetRegionParameterAtIndex | Gets the specified parameter value for the specified region in this variable-pitch helix. |
| Method | InsertRecord | Inserts a record before the specified index in the Region parameters table of this variable-pitch helix. |
| Method | SetRegionParameterAtIndex | Sets the specified parameter for the specified region in this variable-pitch helix. |

[Top](#topBookmark)

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::InsertHelix Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHelix.html)
[IFeatureManager::InsertVariablePitchHelix Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVariablePitchHelix.html)
[IFeatureManager::AddVariablePitchHelixFirstPitchAndDiameter Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixFirstPitchAndDiameter.html)
[IFeatureManager::AddVariablePitchHelixSegment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixSegment.html)
[IFeatureManager::EndVariablePitchHelix Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EndVariablePitchHelix.html)
