---
title: "ICWJoints Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html"
---

# ICWJoints Interface Members

The following tables list the members exposed by [ICWJoints](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | IncludeAllSelectedBeam | Get or sets whether to include all beams in the joints. |
| Property | IncludeDisplayNeutralAxis | Gets or sets whether to show or hide a neutral axis for each beam. |
| Property | IncludeKeepModifiedJointOnUpdate | Gets or sets whether to save modifications made to the joints. |
| Property | IncludeTreatAsJointForClearanceLessThan | Gets or sets whether to overwrite the optimal tolerance value for non-touching structural members within a certain distance, also called pinballs. |
| Property | IncludeUserSelectedBeam | Gets or sets whether to include only the user-selected beams. |
| Property | PinBallRadius | Gets or sets the optimal tolerance value for non-touching structural members within a certain distance, which is also referred to as a pinball. |
| Property | PinBallRadiusUnit | Gets or sets the unit for the optimal tolerance value for non-touching structural members within a certain distance, which is also referred to as a pinball. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CalculateJoints | Calculates the joints at the free ends of structural members and at the intersection of two or more structural members. |
| Method | DeleteJoint | Deletes the specified joint. |
| Method | InsertBeamEntity | Inserts the specified beam in the joints. |
| Method | JointsBeginEdit | Begins editing of joints. |
| Method | JointsEndEdit | Ends editing of joints. |
| Method | RemoveBeamEntityAt | Removes the specified beam from the joints. |

[Top](#topBookmark)

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
