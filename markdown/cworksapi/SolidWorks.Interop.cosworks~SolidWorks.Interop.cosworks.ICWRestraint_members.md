---
title: "ICWRestraint Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html"
---

# ICWRestraint Interface Members

The following tables list the members exposed by [ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | RestraintType | Gets or sets the type of this restraint. |
| Property | Unit | Gets or sets the units of translation or rotation for this restraint. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetCoordinateType | Gets the coordinate system type for this restraint. |
| Method | GetReverseDirections | Obsolete. Superseded by ICWRestraint::GetReverseDirections2 . |
| Method | GetReverseDirections2 | Gets whether to reverse the translation and rotation component directions for this restraint. |
| Method | GetRotationComponentsValues | Obsolete. Superseded by ICWRestraint::GetRotationComponentsValues2 . |
| Method | GetRotationComponentsValues2 | Gets the rotational components of this restraint. |
| Method | GetTimeCurve | Gets the time curve data for this restraint. |
| Method | GetTranslationComponentsValues | Obsolete. Superseded by ICWRestraint::GetTranslationComponentsValues2 . |
| Method | GetTranslationComponentsValues2 | Gets the translation components for the restraint. |
| Method | InsertEntity | Inserts an entity in the restraint. |
| Method | RemoveEntity | Removes the entity at the specified index from the restraint. |
| Method | RestraintBeginEdit | Starts editing a restraint. |
| Method | RestraintEndEdit | Ends editing a restraint. |
| Method | SetReferenceGeometry | Sets the direction reference for this restraint. |
| Method | SetReverseDirections | Obsolete. Superseded by ICWRestraint::SetReverseDirections2 . |
| Method | SetReverseDirections2 | Sets whether to reverse the translation and rotation component directions for this restraint. |
| Method | SetRotationComponentsValues | Obsolete. Superseded by ICWRestraint::SetRotationComponentsValues2 . |
| Method | SetRotationComponentsValues2 | Sets the rotational components of this restraint. |
| Method | SetTimeCurve | Obsolete. Superseded by ICWRestraint::SetTimeCurve2 . |
| Method | SetTimeCurve2 | Sets the time curve data for this restraint. |
| Method | SetTranslationComponentsValues | Obsolete. Superseded by ICWRestraint::SetTranslationComponentsValues2 . |
| Method | SetTranslationComponentsValues2 | Sets the translation components for this restraint. |

[Top](#topBookmark)

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
