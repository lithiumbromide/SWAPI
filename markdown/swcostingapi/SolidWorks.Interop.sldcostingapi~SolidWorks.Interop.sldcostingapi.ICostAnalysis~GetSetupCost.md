---
title: "GetSetupCost Method (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "GetSetupCost"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetSetupCost.html"
---

# GetSetupCost Method (ICostAnalysis)

Gets the tool setup cost in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSetupCost() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Double

value = instance.GetSetupCost()
```

### C#

```csharp
System.double GetSetupCost()
```

### C++/CLI

```cpp
System.double GetSetupCost();
```

### Return Value

Tool setup cost

## VBA Syntax

See [CostAnalysis::GetSetupCost](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~GetSetupCost.html).

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
[ICostAnalysis::GetManufacturingCost Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetManufacturingCost.html)
[ICostAnalysis::GetMaterialCost Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetMaterialCost.html)
[ICostAnalysis::GetTotalCostToCharge Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetTotalCostToCharge.html)
[ICostAnalysis::GetTotalCostToManufacture Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetTotalCostToManufacture.html)
[ICostBody::AssignCustomCost Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~AssignCustomCost.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
