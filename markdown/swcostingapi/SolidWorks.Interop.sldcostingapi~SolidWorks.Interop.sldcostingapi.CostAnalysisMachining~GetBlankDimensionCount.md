---
title: "GetBlankDimensionCount Method (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "GetBlankDimensionCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~GetBlankDimensionCount.html"
---

# GetBlankDimensionCount Method (CostAnalysisMachining)

Gets the number of dimensions for a blank required to produce a body using the specified stock type for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBlankDimensionCount( _
   ByVal StockType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim StockType As System.Integer
Dim value As System.Integer

value = instance.GetBlankDimensionCount(StockType)
```

### C#

```csharp
System.int GetBlankDimensionCount(
   System.int StockType
)
```

### C++/CLI

```cpp
System.int GetBlankDimensionCount(
   System.int StockType
)
```

### Parameters

- `StockType`: Stock type as defined in [swcStockType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcStockType_e.html)

### Return Value

Number of dimensions for a blank required to produce a body using the specified stock type

## VBA Syntax

See [CostAnalysisMachining::GetBlankDimensionCount](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~GetBlankDimensionCount.html).

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
