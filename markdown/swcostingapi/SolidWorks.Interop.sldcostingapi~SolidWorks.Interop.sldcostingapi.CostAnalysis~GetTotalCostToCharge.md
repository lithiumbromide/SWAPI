---
title: "GetTotalCostToCharge Method (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "GetTotalCostToCharge"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~GetTotalCostToCharge.html"
---

# GetTotalCostToCharge Method (CostAnalysis)

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
Dim instance As CostAnalysis
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

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
