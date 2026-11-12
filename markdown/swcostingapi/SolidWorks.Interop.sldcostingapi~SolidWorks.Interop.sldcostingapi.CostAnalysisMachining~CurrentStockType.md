---
title: "CurrentStockType Property (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "CurrentStockType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~CurrentStockType.html"
---

# CurrentStockType Property (CostAnalysisMachining)

Gets or sets the current stock type for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentStockType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim value As System.Integer

instance.CurrentStockType = value

value = instance.CurrentStockType
```

### C#

```csharp
System.int CurrentStockType {get; set;}
```

### C++/CLI

```cpp
property System.int CurrentStockType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Current stock type as defined in [swcStockType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcStockType_e.html)

## VBA Syntax

See [CostAnalysisMachining::CurrentStockType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~CurrentStockType.html).

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
