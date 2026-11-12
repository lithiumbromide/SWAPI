---
title: "ICostAnalysisMachining Interface Members"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining_members"
member: ""
kind: "members"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html"
---

# ICostAnalysisMachining Interface Members

The following tables list the members exposed by [ICostAnalysisMachining](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BlankSize | Gets or sets the size of the blank for this machining Costing analysis. |
| Property | CurrentMaterial | Gets or sets the name of the material for this machining Costing analysis. |
| Property | CurrentMaterialClass | Gets or sets the name of the material class for this machining Costing analysis. |
| Property | CurrentPlateThickness | Gets or sets the thickness of the plate for this machining Costing analysis. |
| Property | CurrentStockType | Gets or sets the current stock type for this machining Costing analysis. |
| Property | CustomStockBodyName | Gets or sets the name of the configuration or reference part for a custom stock body in a machining Costing analysis. |
| Property | CustomStockCostInfoType | Gets or sets the type of custom stock cost for this machining Costing analysis. |
| Property | CustomStockCustomCost | Gets or sets the custom stock cost for this machining Costing analysis. |
| Property | CustomStockImportType | Gets and sets the custom stock import type for this machining Costing analysis. |
| Property | IBlankSize | Gets or sets the size of the blank for this machining Costing analysis. |
| Property | IMargins | Gets or sets the margins for the stock type for this machining Costing analysis. |
| Property | Margins | Gets or sets the margins for the stock type for this machining Costing analysis. |
| Property | PreviewShown | Gets or sets whether to display a preview of the blank for this machining Costing analysis. |
| Property | ShopRate | Gets or sets the hourly shop rate for this machining Costing analysis. |
| Property | ShopRateApplied | Gets or sets whether an hourly shop rate is applied to this machining Costing analysis. |
| Property | SpecificSizeEnabled | Gets or sets whether a user can specify the X, Y, and Z block dimensions to add to the tightest fitting stock faces for this machining Cost analysis. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetBlankDimensionCount | Gets the number of dimensions for a blank required to produce a body using the specified stock type for this machining Costing analysis. |
| Method | GetMarginDimensionCount | Gets the number of dimensions for the margins for the stock type for this machining Costing analysis. |
| Method | GetMaterialClasses | Gets the names of the material classes from the Costing template for this machining Costing analysis. |
| Method | GetMaterialClassesCount | Gets the number of material classes from the Costing template for this machining Costing analysis. |
| Method | GetMaterialCount | Gets the number of materials in the specified class from the Costing template for this machining Costing analysis. |
| Method | GetMaterials | Gets the names of the materials in the specified class from the Costing template for this machining Costing analysis. |
| Method | GetMinimumBlankSize | Gets the dimensions of the smallest possible blank required to produce a body using the currently selected stock type for this machining Costing analysis. |
| Method | GetStockTypeCount | Gets the number of stock types for the specified material from the Costing template for this machining Costing analysis. |
| Method | GetStockTypes | Gets the stock types for the specified material from the Costing template for this machining Costing analysis. |
| Method | IGetMaterialClasses | Gets the names of the material classes from the Costing template for this machining Costing analysis. |
| Method | IGetMaterials | Gets the names of the materials in the specified class from the Costing template for this machining Costing analysis. |
| Method | IGetMinimumBlankSize | Gets the dimensions of the smallest possible blank required to produce a body using the currently selected stock type for this machining Costing analysis. |
| Method | IGetStockTypes | Gets the stock types for the specified material from the Costing template for this machining Costing analysis. |
| Method | ResetShopRate | Resets the hourly shop rate to the default hourly shop rate set in the machining template for this machining Costing analysis. |

[Top](#topBookmark)

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
