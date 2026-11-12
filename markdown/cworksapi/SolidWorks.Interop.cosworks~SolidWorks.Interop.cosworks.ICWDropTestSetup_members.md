---
title: "ICWDropTestSetup Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html"
---

# ICWDropTestSetup Interface Members

The following tables list the members exposed by [ICWDropTestSetup](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CriticalDampingRatio | Gets or sets the critical damping ratio for the drop test study. |
| Property | DropHeight | Gets or sets the height from which the model is dropped to the floor. |
| Property | DropHeightType | Gets or sets the drop height type. |
| Property | DropHeightUnit | Gets or sets the units of drop height. |
| Property | DropType | Gets or sets the type of input to specify for this drop test setup. |
| Property | FlipGravityDirection | Obsolete. Superseded by ICWDropTestSetup::FlipGravityDirection2 . |
| Property | FlipGravityDirection2 | Gets or sets whether to reverse the direction of gravity. |
| Property | FlipVelocityDirection | Obsolete. Superseded by ICWDropTestSetup::FlipVelocityDirection2 . |
| Property | FlipVelocityDirection2 | Gets or sets whether to reverse the direction of the velocity at impact. |
| Property | FrictionCoefficient | Gets or sets the coefficient of friction between the model and the impact plane. |
| Property | Gravity | Gets or sets the magnitude of gravity. |
| Property | GravityUnit | Gets or sets the units of gravity. |
| Property | MassDensity | Gets or sets the mass density of the impact layer. |
| Property | NormalStiffness | Gets or sets the stiffness per unit area that is normal to the impact plane. |
| Property | StiffnessUnit | Gets or sets the units of stiffness. |
| Property | TangentialStiffness | Gets or sets the stiffness per unit area that is parallel to the impact plane. |
| Property | TargetOrientationType | Gets or sets the orientation of the impact plane. |
| Property | TargetStiffnessType | Gets or sets the stiffness type of the impact plane. |
| Property | TargetThickness | Gets or sets the thickness of the impact layer. |
| Property | ThicknessUnit | Gets or sets the units of thickness. |
| Property | Velocity | Gets or sets the magnitude of velocity at impact. |
| Property | VelocityUnit | Gets or sets the units of velocity. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | DropTestSetupBeginEdit | Starts editing the drop test setup. |
| Method | DropTestSetupEndEdit | Ends editing the drop test setup. |
| Method | SetEntityForGravityDirection | Obsolete. Superseded by ICWDropTestSetup::SetEntityForGravityDirection2 . |
| Method | SetEntityForGravityDirection2 | Sets the face, edge, or plane reference to determine the direction of gravity. |
| Method | SetEntityForTargetOrientation | Obsolete. Superseded by ICWDropTestSetup::SetEntityForTargetOrientation2 . |
| Method | SetEntityForTargetOrientation2 | Sets the orientation reference for the impact plane. |
| Method | SetEntityForVelocityDirection | Obsolete. Superseded by ICWDropTestSetup::SetEntityForVelocityDirection2 . |
| Method | SetEntityForVelocityDirection2 | Sets the face, edge, or plane reference to determine the direction of the velocity at impact. |

[Top](#topBookmark)

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWDropTestResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions.html)
[ICWDropTestStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions.html)
