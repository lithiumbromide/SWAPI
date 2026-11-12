---
title: "ICostFeature Interface Members"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature_members"
member: ""
kind: "members"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature_members.html"
---

# ICostFeature Interface Members

The following tables list the members exposed by [ICostFeature](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CombinedCost | Gets or sets the cost of this Costing feature or operation, including the combined cost of Costing child features and operations. |
| Property | CombinedTime | Gets or sets the time for this Costing feature or operation, including the combined times of Costing child features and operations. |
| Property | Description | Gets or sets the description of this Costing feature, including information about selected sub-operation options. |
| Property | IsOverridden | Gets whether a cost override was applied to this Costing feature. |
| Property | IsSetup | Gets whether this Costing feature is a setup-related Costing feature. |
| Property | Name | Gets or sets the name of the Costing feature in the CostingManager. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetFirstSubFeature | Gets the first child feature that belongs to the Costing feature in the CostingManager. |
| Method | GetNextFeature | Gets the next Costing feature in the CostingManager. |
| Method | GetNextSubFeature | Gets the next Costing child feature from the owner of this Costing child feature in the CostingManager. |
| Method | GetType | Gets the type of Costing feature in the CostingManager. |
| Method | RemoveOverrideCostTime | Removes the cost override and the time required for each operation to manufacture this Costing feature. |
| Method | SelectFaces | Selects the faces in the part affected by this Costing feature. |

[Top](#topBookmark)

## See Also

[ICostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
[ICostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody.html)
[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
