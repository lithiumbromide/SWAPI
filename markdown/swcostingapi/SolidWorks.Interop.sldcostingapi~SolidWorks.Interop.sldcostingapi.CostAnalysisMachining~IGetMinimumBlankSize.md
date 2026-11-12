---
title: "IGetMinimumBlankSize Method (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "IGetMinimumBlankSize"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~IGetMinimumBlankSize.html"
---

# IGetMinimumBlankSize Method (CostAnalysisMachining)

Gets the dimensions of the smallest possible blank required to produce a body using the [currently selected stock type](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html) for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMinimumBlankSize( _
   ByVal NumDimensions As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim NumDimensions As System.Integer
Dim value As System.Double

value = instance.IGetMinimumBlankSize(NumDimensions)
```

### C#

```csharp
System.double IGetMinimumBlankSize(
   System.int NumDimensions
)
```

### C++/CLI

```cpp
System.double IGetMinimumBlankSize(
   System.int NumDimensions
)
```

### Parameters

- `NumDimensions`: Number of dimensions

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles of the dimensions of the smallest possible blank required to produce a body using the currently selected stock type

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [ICostAnalysisMachining::GetBlankDimensionCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~GetBlankDimensionCount.html) to get the NumDimensions value.

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
