---
title: "ICWBearingConnector Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html"
---

# ICWBearingConnector Interface Members

The following tables list the members exposed by [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AllowLenByDiamRatioGreaterThan2ForShaft | Sets whether to allow (shaft length)/(shaft diameter) > 2. |
| Property | AllowShaftByBearingRatioGreaterThan2 | Sets whether to allow (shaft length)/(bearing length) > 2. |
| Property | AxialStiffnessValue | Sets the total axial stiffness value for this bearing connector. |
| Property | ConnectionType | Sets the type of this bearing connector. |
| Property | LateralStiffnessValue | Sets the total rotational (lateral) stiffness value for this bearing connector. |
| Property | RotationalStiffnessValue | Obsolete. Superseded by ICWBearingConnector::LateralStiffnessValue . |
| Property | StabilizeShaftRotation | Sets whether to stabilize the shaft rotation of this bearing connector. |
| Property | StabilizeShaftRotationalStiffnessValue | Sets the user-defined shaft rotation stabilization value. |
| Property | StabilizeShaftRotationType | Sets the type of shaft rotation stabilization. |
| Property | StiffnessType | Sets the stiffness type of this bearing connecgtor. |
| Property | TiltStiffnessValue | Sets the tilt stiffness value for this bearing connector. |
| Property | UnitType | Sets the unit type for this bearing connector. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | BeginEdit | Starts editing this bearing connector. |
| Method | EndEdit | Stops editing this bearing connector. |
| Method | GetLastErrorCode | Gets the last error thrown for this bearing connector. |
| Method | PerformAdvanceValidations | Calculates (shaft length)/(shaft diameter) and (shaft length)/(bearing length). |
| Method | ReplaceCircularFaceForShaft | Replaces the circular face of the shaft with the specified circular face. |
| Method | ReplaceCircularFaceOrEdgeForHousing | Replaces the housing circular face or edge with the specified face or edge. |

[Top](#topBookmark)

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
