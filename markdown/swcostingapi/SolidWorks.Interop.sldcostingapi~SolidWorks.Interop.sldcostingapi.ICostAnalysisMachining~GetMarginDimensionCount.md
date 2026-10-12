---
title: "GetMarginDimensionCount Method (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "GetMarginDimensionCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMarginDimensionCount.html"
---

# GetMarginDimensionCount Method (ICostAnalysisMachining)

Gets the number of dimensions for the margins for the [stock type](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html) for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMarginDimensionCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim value As System.Integer

value = instance.GetMarginDimensionCount()
```

### C#

```csharp
System.int GetMarginDimensionCount()
```

### C++/CLI

```cpp
System.int GetMarginDimensionCount();
```

### Return Value

Number of dimensions for the margins for the stock type

## VBA Syntax

See [CostAnalysisMachining::GetMarginDimensionCount](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~GetMarginDimensionCount.html).

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::Margins Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~Margins.html)
[ICostAnalysisMachining::IMargins Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IMargins.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
