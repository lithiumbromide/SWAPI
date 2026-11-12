---
title: "ICostPart Interface Members"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart_members"
member: ""
kind: "members"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html"
---

# ICostPart Interface Members

The following tables list the members exposed by [ICostPart](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ActiveBody | Gets the active Costing body in this Costing part. |
| Property | TemplateOverrides | Gets the ITemplateOverrides object. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ActivateBody | Activates the specified Costing body in the Costing part, which allows modifications to its Costing analysis. |
| Method | CreateCostAnalysis | Creates a new Costing analysis for this Costing part using the specified Costing template. |
| Method | GetBodies | Gets the Costing bodies in this Costing part. |
| Method | GetBodyCount | Gets the number of Costing bodies in this Costing part, including excluded and custom Costing bodies. |
| Method | GetCostAnalysis | Accesses the existing Cost analysis for this Costing part. |
| Method | GetCostingMethod | Gets the manufacturing method for this Costing part. |
| Method | IGetBodies | Gets the Costing bodies in this Costing part. |
| Method | IncludeBody | Gets whether to include the specified Costing body in this Costing part in the Costing analysis. |
| Method | IUpdateCostForAllBodies | Updates the Costing data for all of the bodies in this Costing Part. |
| Method | SetCostingMethod | Sets the manufacturing method for this Costing part. |
| Method | UpdateCostForAllBodies | Updates the Costing data for all of the bodies in this Costing Part. |

[Top](#topBookmark)

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
[ICostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody.html)
[ICostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html)
