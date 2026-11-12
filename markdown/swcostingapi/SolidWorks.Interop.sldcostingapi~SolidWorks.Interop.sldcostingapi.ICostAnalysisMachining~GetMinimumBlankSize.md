---
title: "GetMinimumBlankSize Method (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "GetMinimumBlankSize"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMinimumBlankSize.html"
---

# GetMinimumBlankSize Method (ICostAnalysisMachining)

Gets the dimensions of the smallest possible blank required to produce a body using the [currently selected stock type](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html) for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinimumBlankSize() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
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

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::IGetMinimumBlankSize Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMinimumBlankSize.html)
[ICostAnalysisMachining::BlankSize Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~BlankSize.html)
[ICostAnalysisMachining::IBlankSize Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IBlankSize.html)
[ICostAnalysisMachining::GetBlankDimensionCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetBlankDimensionCount.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
