---
title: "ICostAnalysis Interface Members"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis_members"
member: ""
kind: "members"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html"
---

# ICostAnalysis Interface Members

The following tables list the members exposed by [ICostAnalysis](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CostingTemplateName | Gets the name of the Costing template for this Costing analysis. |
| Property | CostingType | Gets the Costing type from the Costing template for this Costing analysis. |
| Property | CurrencyCode | Gets the 3-letter currency code from the Costing template for this Costing analysis. |
| Property | CurrencyName | Gets the name of the currency from the Costing template for this Costing analysis. |
| Property | CurrencySeparator | Gets the delimiter for the currency from the Costing template for this Costing analysis. |
| Property | LengthUnit | Gets the unit for the length from the Costing template for this Costing analysis. |
| Property | LotSize | Gets or sets the quantity of parts to produce per batch for this Costing analysis. |
| Property | MarkUpPercent | Gets or sets the markup percentage for this Costing analysis. |
| Property | MarkUpType | Gets or sets the method of markup for this Costing analysis. |
| Property | MassUnit | Gets the unit of mass from the Costing template for this Costing analysis. |
| Property | TotalQuantity | Gets or sets the total quantity of parts to produce for this Costing analysis. |
| Property | UnitSystem | Gets the unit system from the Costing template for this Costing analysis. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetFirstCostFeature | Gets the first Costing feature in the CostingManager in this Costing analysis. |
| Method | GetManufacturingCost | Gets the total manufacturing cost in this Costing analysis. |
| Method | GetMaterialCost | Gets the costs of the materials in this Costing analysis. |
| Method | GetSetupCost | Gets the tool setup cost in this Costing analysis. |
| Method | GetSpecificAnalysis | Gets the specific Costing analysis in this Costing analysis. |
| Method | GetTotalCostToCharge | Gets the total cost to charge the customer, including: materials , manufacturing , setup , markup , and shop-rate costs in this Costing analysis. |
| Method | GetTotalCostToManufacture | Gets the total cost to manufacture the part: including material , manufacturing , and setup costs excluding markup and shop-rate costs in this Costing analysis. |

[Top](#topBookmark)

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
