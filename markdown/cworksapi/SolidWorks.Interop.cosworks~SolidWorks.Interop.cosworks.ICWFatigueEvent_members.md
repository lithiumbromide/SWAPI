---
title: "ICWFatigueEvent Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html"
---

# ICWFatigueEvent Interface Members

The following tables list the members exposed by [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Cycles | Obsolete. Superseded by ICWFatigueEvent::Cycles2 . |
| Property | Cycles2 | Gets or sets the number of cycles associated with this fatigue event. |
| Property | LoadingRatio | Gets or sets the loading ratio for this fatigue event. |
| Property | LoadingType | Gets or sets the type of fatigue loading to determine the stress peaks and alternating stresses. |
| Property | Name | Gets the name of this fatigue event. |
| Property | NoOfRepeats | Gets or sets the number of times to repeat the curve data. |
| Property | StartTimes | Gets or sets the start time for this fatigue event. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | FatigueEventBeginEdit | Starts editing the fatigue event. |
| Method | FatigueEventEndEdit | Ends editing the fatigue event. |
| Method | GetLoadHistoryCurve | Gets the load history curve data for this variable amplitude fatigue event. |
| Method | GetStudyAssociationData | Gets the study association data for this fatigue event. |
| Method | SetLoadHistoryCurve | Sets the load history curve data for this variable amplitude fatigue event. |
| Method | SetStudyAssociationData | Sets the study association data for this fatigue event. |
| Method | SuppressUnSuppress | Toggles the suppression of this fatigue event in the study. |

[Top](#topBookmark)

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
