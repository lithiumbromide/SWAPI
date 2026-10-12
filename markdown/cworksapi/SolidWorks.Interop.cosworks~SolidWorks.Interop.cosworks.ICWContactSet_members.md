---
title: "ICWContactSet Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html"
---

# ICWContactSet Interface Members

The following tables list the members exposed by [ICWContactSet](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AxialStiffnessValue | Gets or sets the wall axial stiffness value for this flexible virtual wall contact set. |
| Property | ClearanceUnit | Gets or sets the units of clearance for this contact set. |
| Property | ClearanceValue | Gets or sets the clearance (gap) value for this contact set. |
| Property | ContactName | Gets the name of this contact set. |
| Property | ContactSetType | Gets or sets the type of this contact set. |
| Property | FrictionValue | Gets or sets the friction coefficient for this contact set. |
| Property | GapType | Gets or sets the gap type associated with this contact set. |
| Property | IncludeFriction | Obsolete. Superseded by ICWContactSet::IncludeFriction2 . |
| Property | IncludeFriction2 | Sets whether to include friction in this contact set. |
| Property | Options | Gets or sets the advanced options for this contact set. |
| Property | ResistanceType | Gets or sets the thermal resistance type for this thermal resistance contact set. |
| Property | ResistanceUnit | Gets or sets the unit system for this thermal resistance contact set. |
| Property | ResistanceValue | Gets or sets the thermal resistance value for this thermal resistance contact set. |
| Property | SourceEntityCount | Gets the number of source entities in this contact set. |
| Property | State | Gets the suppression state of this contact set. |
| Property | TangentialStiffnessValue | Gets or sets the wall shear stiffness value for this flexible virtual wall contact set. |
| Property | TargetEntityCount | Gets the number of target entities in this contact set. |
| Property | WallFriction | Gets or sets the coefficient of friction for this contact set with a rigid virtual wall. |
| Property | WallStiffnessUnit | Gets or sets the wall stiffness units of this contact set. |
| Property | WallType | Gets or sets the wall type of this contact set. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ContactSetBeginEdit | Starts editing this contact set. |
| Method | ContactSetEndEdit | Ends editing this contact set. |
| Method | GetSourceEntityAt | Gets the entity type and source entity of this contact set at the specified index. |
| Method | GetTargetEntityAt | Gets the entity type and target entity of this contact set at the specified index. |
| Method | InsertSourceEntity | Inserts the specified source entity into this contact set. |
| Method | InsertTargetEntity | Inserts the specified target entity into this contact set. |
| Method | RemoveSourceEntity | Removes a source entity at the specified index from this contact set. |
| Method | RemoveTargetEntity | Removes a target entity at the specified index from this contact set. |
| Method | SuppressUnSuppress | Suppresses or unsuppresses this contact set depending on its state . |

[Top](#topBookmark)

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
