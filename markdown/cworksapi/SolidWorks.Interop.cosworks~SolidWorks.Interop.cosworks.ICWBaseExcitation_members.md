---
title: "ICWBaseExcitation Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html"
---

# ICWBaseExcitation Interface Members

The following tables list the members exposed by [ICWBaseExcitation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BaseExcitationType | Gets or sets the type of this base excitation. |
| Property | FixtureNameInSelectedExcitation | Gets or sets the fixture name for this selected excitation. |
| Property | PhaseAngle | Gets or sets the phase angle of this base excitation. |
| Property | PhaseAngleUnit | Gets or sets the units of phase angle for this base excitation. |
| Property | Unit | Gets or sets the units for this base excitation. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | BaseExcitationBeginEdit | Starts editing base excitation. |
| Method | BaseExcitationEndEdit | Ends editing base excitation. |
| Method | GetExcitationDirections | Obsolete. Superseded by ICWBaseExcitation::GetExcitationDirections2 . |
| Method | GetExcitationDirections2 | Gets the directions in which this excitation is applied. |
| Method | GetExcitationDirectionValues | Gets the excitation values in each direction. |
| Method | GetExcitationReverseDirections | Obsolete. Superseded by ICWBaseExcitation::GetExcitationReverseDirections2 . |
| Method | GetExcitationReverseDirections2 | Gets whether to reverse base excitation directions. |
| Method | GetTimeOrFrequencyCurve | Gets the variation of base excitation with frequency or time. |
| Method | SetDirectionEntityForUniformExcitation | Sets the face, edge, or plane in whose direction the base excitation is uniformly applied to all restrained locations. |
| Method | SetExcitationDirections | Obsolete. Superseded by ICWBaseExcitation::setExcitationDirections2 . |
| Method | SetExcitationDirections2 | Sets the excitation directions. |
| Method | SetExcitationDirectionValues | Sets the excitation direction values. |
| Method | SetExcitationReverseDirections | Obsolete. Superseded by ICWBaseExcitation::SetExcitationReverseDirections2 . |
| Method | SetExcitationReverseDirections2 | Sets whether to reverse base excitation directions. |
| Method | SetTimeOrFrequencyCurve | Obsolete. Superseded by ICWBaseExcitation::SetTimeOrFrequencyCurve2 . |
| Method | SetTimeOrFrequencyCurve2 | Sets the variation of base excitation with time or frequency. |

[Top](#topBookmark)

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
