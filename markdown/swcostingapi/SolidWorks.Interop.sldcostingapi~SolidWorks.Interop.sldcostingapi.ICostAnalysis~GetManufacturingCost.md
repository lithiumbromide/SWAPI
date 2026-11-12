---
title: "GetManufacturingCost Method (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "GetManufacturingCost"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetManufacturingCost.html"
---

# GetManufacturingCost Method (ICostAnalysis)

Gets the total manufacturing cost in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetManufacturingCost() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Double

value = instance.GetManufacturingCost()
```

### C#

```csharp
System.double GetManufacturingCost()
```

### C++/CLI

```cpp
System.double GetManufacturingCost();
```

### Return Value

Total manufacturing cost

## VBA Syntax

See [CostAnalysis::GetManufacturingCost](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~GetManufacturingCost.html).

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
[ICostAnalysis::GetMaterialCost Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetMaterialCost.html)
[ICostAnalysis::GetSetupCost Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetSetupCost.html)
[ICostAnalysis::GetTotalCostToCharge Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetTotalCostToCharge.html)
[ICostAnalysis::GetTotalCostToManufacture Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetTotalCostToManufacture.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
