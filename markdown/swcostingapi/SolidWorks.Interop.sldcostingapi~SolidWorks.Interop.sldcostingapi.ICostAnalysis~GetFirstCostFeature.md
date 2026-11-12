---
title: "GetFirstCostFeature Method (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "GetFirstCostFeature"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetFirstCostFeature.html"
---

# GetFirstCostFeature Method (ICostAnalysis)

Gets the first Costing feature in the CostingManager in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstCostFeature() As CostFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As CostFeature

value = instance.GetFirstCostFeature()
```

### C#

```csharp
CostFeature GetFirstCostFeature()
```

### C++/CLI

```cpp
CostFeature^ GetFirstCostFeature();
```

### Return Value

First [Costing feature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature.html) or null if no Costing features exist

## VBA Syntax

See [CostAnalysis::GetFirstCostFeature](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~GetFirstCostFeature.html).

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
[ICostFeature::GetNextFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetNextFeature.html)
[ICostFeature::GetFirstSubFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetFirstSubFeature.html)
[ICostFeature::GetNextSubFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetNextSubFeature.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
