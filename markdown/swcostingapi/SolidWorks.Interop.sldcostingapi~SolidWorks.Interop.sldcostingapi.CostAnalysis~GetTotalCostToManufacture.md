---
title: "GetTotalCostToManufacture Method (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "GetTotalCostToManufacture"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~GetTotalCostToManufacture.html"
---

# GetTotalCostToManufacture Method (CostAnalysis)

Gets the total cost to manufacture the part:

- including [material](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~GetMaterialCost.html), [manufacturing](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~GetManufacturingCost.html), and [setup](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~GetSetupCost.html) costs
- excluding [markup](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~MarkUpPercent.html) and [shop-rate](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~ShopRate.html) costs

in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTotalCostToManufacture() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.Double

value = instance.GetTotalCostToManufacture()
```

### C#

```csharp
System.double GetTotalCostToManufacture()
```

### C++/CLI

```cpp
System.double GetTotalCostToManufacture();
```

### Return Value

Total cost to manufacture the part

## VBA Syntax

See [CostAnalysis::GetTotalCostToManufacture](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~GetTotalCostToManufacture.html).

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
