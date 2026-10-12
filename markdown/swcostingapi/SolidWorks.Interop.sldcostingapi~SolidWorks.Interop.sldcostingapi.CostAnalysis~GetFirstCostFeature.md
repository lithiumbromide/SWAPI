---
title: "GetFirstCostFeature Method (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "GetFirstCostFeature"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~GetFirstCostFeature.html"
---

# GetFirstCostFeature Method (CostAnalysis)

Gets the first Costing feature in the CostingManager in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstCostFeature() As CostFeature
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
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

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
