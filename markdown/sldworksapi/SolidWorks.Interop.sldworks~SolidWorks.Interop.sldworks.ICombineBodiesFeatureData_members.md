---
title: "ICombineBodiesFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICombineBodiesFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html"
---

# ICombineBodiesFeatureData Interface Members

The following tables list the members exposed by [ICombineBodiesFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BodiesToCombine | Gets or sets the bodies to combine. |
| Property | MainBody | Gets or sets the main body to keep when subtracting bodies from this combine feature. |
| Property | OperationType | Gets or sets how to combine multiple solid bodies for a combine feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this combine feature. |
| Method | GetBodiesToCombineCount | Gets the number of bodies to combine. |
| Method | IGetBodiesToCombine | Gets the bodies to combine. |
| Method | ISetBodiesToCombine | Sets the bodies to combine. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this combine feature. |

[Top](#topBookmark)

## See Also

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::IInsertCombineFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertCombineFeature.html)
[IFeatureManager::InsertCombineFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCombineFeature.html)
