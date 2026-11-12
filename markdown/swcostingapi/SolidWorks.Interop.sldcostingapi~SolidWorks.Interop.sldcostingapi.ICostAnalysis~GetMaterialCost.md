---
title: "GetMaterialCost Method (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "GetMaterialCost"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetMaterialCost.html"
---

# GetMaterialCost Method (ICostAnalysis)

Gets the costs of the materials in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialCost() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Double

value = instance.GetMaterialCost()
```

### C#

```csharp
System.double GetMaterialCost()
```

### C++/CLI

```cpp
System.double GetMaterialCost();
```

### Return Value

Costs of the materials

## VBA Syntax

See [CostAnalysis::GetMaterialCost](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~GetMaterialCost.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[ICostAnalysis::GetManufacturingCost Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetManufacturingCost.html)
[ICostAnalysis::GetSetupCost Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetSetupCost.html)
[ICostAnalysis::GetTotalCostToCharge Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetTotalCostToCharge.html)
[ICostAnalysis::GetTotalCostToManufacture Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetTotalCostToManufacture.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
