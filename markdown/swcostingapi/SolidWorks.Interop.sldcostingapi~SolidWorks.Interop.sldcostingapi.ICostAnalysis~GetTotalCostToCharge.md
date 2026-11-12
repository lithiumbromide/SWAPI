---
title: "GetTotalCostToCharge Method (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "GetTotalCostToCharge"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetTotalCostToCharge.html"
---

# GetTotalCostToCharge Method (ICostAnalysis)

Gets the total cost to charge the customer, including:

- [materials](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~GetMaterialCost.html),
- [manufacturing](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~GetManufacturingCost.html),
- [setup](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~GetSetupCost.html),
- [markup](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~MarkUpPercent.html), and
- [shop-rate](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~ShopRate.html) costs

in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTotalCostToCharge() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Double

value = instance.GetTotalCostToCharge()
```

### C#

```csharp
System.double GetTotalCostToCharge()
```

### C++/CLI

```cpp
System.double GetTotalCostToCharge();
```

### Return Value

Total cost to charge the customer

## VBA Syntax

See [CostAnalysis::GetTotalCostToCharge](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~GetTotalCostToCharge.html).

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[ICostAnalysis::GetTotalCostToManufacture Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetTotalCostToManufacture.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
