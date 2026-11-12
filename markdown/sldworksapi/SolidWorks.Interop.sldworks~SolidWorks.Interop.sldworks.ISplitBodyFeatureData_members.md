---
title: "ISplitBodyFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html"
---

# ISplitBodyFeatureData Interface Members

The following tables list the members exposed by [ISplitBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Consume | Gets or sets whether the bodies in this Split feature are consumed. |
| Property | OverrideDefaultTemplateSettings | Gets or sets whether to use an alternate template to apply to all new part or assembly files created during the split operation. |
| Property | TemplatePath | Gets or sets the template to use to make this Split feature. |
| Property | TrimTools | Gets the trimming surfaces used as trim tools in this Split feature. NOTE: This property is a get-only property. Set is not implemented . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to a Split feature. |
| Method | GetSplitBodies | Gets the split bodies in this Split feature. |
| Method | GetSplitBodiesCount | Gets the number of split bodies in this Split feature. |
| Method | GetTrimToolsCount | Gets the number of trimming surfaces used as trim tools in this Split feature. |
| Method | IGetSplitBodies | Gets the split bodies for this Split feature. |
| Method | IGetTrimTools | Gets the trimming surfaces used as trim tools in this Split feature. |
| Method | ISetSplitBodies | Obsolete. Superseded by ISplitBodyFeatureData::SetSplitBodies2 . |
| Method | ISetTrimTools | Gets the trimming surfaces used as trim tools in this Split feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this Split feature. |
| Method | SetSplitBodies | Obsolete. Superseded by ISplitBodyFeatureData::SetSplitBodies2 . |
| Method | SetSplitBodies2 | Edits the current split bodies in this Split feature. |

[Top](#topBookmark)

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::PreSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.html)
