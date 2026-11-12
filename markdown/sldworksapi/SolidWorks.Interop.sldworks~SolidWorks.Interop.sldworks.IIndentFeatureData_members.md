---
title: "IIndentFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html"
---

# IIndentFeatureData Interface Members

The following tables list the members exposed by [IIndentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Clearance | Gets or sets the clearance between the target and tool bodies in this indent feature. |
| Property | ClearanceDirection | Gets or sets the direction of the clearance for this indent feature. |
| Property | CutDirection | Gets or sets whether to flip the side of the cut for this indent feature. |
| Property | IsCut | Gets or sets whether to remove the intersection area of the target body . |
| Property | SelectionState | Gets or sets the side of the model to keep or remove. |
| Property | TargetBody | Gets or sets the solid or surface body to indent. |
| Property | Thickness | Gets or sets the thickness of the indent feature. |
| Property | ToolBodyRegion | Gets or sets the tool body region for the indent feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this indent feature. |
| Method | GetBodiesCount | Gets the number of solid or surface bodies for the tool body region . |
| Method | ReleaseSelectionAccess | Releases access to the selections for this indent feature. |

[Top](#topBookmark)

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertIndent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertIndent.html)
