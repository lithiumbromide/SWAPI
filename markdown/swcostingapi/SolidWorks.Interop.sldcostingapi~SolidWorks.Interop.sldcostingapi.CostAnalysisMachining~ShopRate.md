---
title: "ShopRate Property (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "ShopRate"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~ShopRate.html"
---

# ShopRate Property (CostAnalysisMachining)

Gets or sets the hourly shop rate for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShopRate As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim value As System.Double

instance.ShopRate = value

value = instance.ShopRate
```

### C#

```csharp
System.double ShopRate {get; set;}
```

### C++/CLI

```cpp
property System.double ShopRate {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Hourly shop rate

## VBA Syntax

See [CostAnalysisMachining::ShopRate](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~ShopRate.html).

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
