---
title: "IRibFeatureData2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html"
---

# IRibFeatureData2 Interface Members

The following tables list the members exposed by [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Body | Gets or sets the body where the rib is created. |
| Property | DraftAngle | Gets or sets the draft angle for the rib. |
| Property | DraftFromWall | Gets or sets whether to draft the rib from the wall interface or the sketch plane. |
| Property | DraftOutward | Gets or sets whether the rib has an outward draft. |
| Property | EnableDraft | Gets or sets whether the rib has an associated draft. |
| Property | ExtrusionDirection | Gets or sets the direction in which to extrude the rib. |
| Property | FlipSide | Gets or sets whether material is added to the reverse side of the rib. |
| Property | IsTwoSided | Gets or sets whether the rib is created on two sides of the midplane or in a single direction (see IRibFeatureData2::ReverseThicknessDir ). |
| Property | RefSketchIndex | Gets or sets which sketch segment defines the draft direction of the rib feature. |
| Property | ReverseThicknessDir | Gets or sets whether the extrusion is on the reverse side of this single-sided rib. |
| Property | Thickness | Gets or set the overall thickness of the rib. |
| Property | Type | Gets or sets the type of rib. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the the selections for this rib feature. |
| Method | IAccessSelections | Gains access to the the selections for this rib feature. |
| Method | NextReference | Cycles through the possible sketch entities that can be used to define the draft, if it is used, for ribs with multiple contours. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this rib feature. |

[Top](#topBookmark)

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertRib Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRib.html)
