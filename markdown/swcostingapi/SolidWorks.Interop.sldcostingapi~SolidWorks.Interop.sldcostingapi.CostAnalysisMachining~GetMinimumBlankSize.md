---
title: "GetMinimumBlankSize Method (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "GetMinimumBlankSize"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~GetMinimumBlankSize.html"
---

# GetMinimumBlankSize Method (CostAnalysisMachining)

Gets the dimensions of the smallest possible blank required to produce a body using the [currently selected stock type](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html) for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinimumBlankSize() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim value As System.Object

value = instance.GetMinimumBlankSize()
```

### C#

```csharp
System.object GetMinimumBlankSize()
```

### C++/CLI

```cpp
System.Object^ GetMinimumBlankSize();
```

### Return Value

Array of doubles of the dimensions of the smallest possible blank required to produce a body using the currently selected stock type

## VBA Syntax

See [CostAnalysisMachining::GetMinimumBlankSize](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~GetMinimumBlankSize.html).

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
