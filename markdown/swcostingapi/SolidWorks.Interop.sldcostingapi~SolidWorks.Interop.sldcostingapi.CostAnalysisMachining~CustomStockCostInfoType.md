---
title: "CustomStockCostInfoType Property (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "CustomStockCostInfoType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~CustomStockCostInfoType.html"
---

# CustomStockCostInfoType Property (CostAnalysisMachining)

Gets or sets the type of custom stock cost for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomStockCostInfoType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim value As System.Integer

instance.CustomStockCostInfoType = value

value = instance.CustomStockCostInfoType
```

### C#

```csharp
System.int CustomStockCostInfoType {get; set;}
```

### C++/CLI

```cpp
property System.int CustomStockCostInfoType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of custom stock cost as defined in [swcCustomStockCostInfoType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcCustomStockCostInfoType_e.html)

## VBA Syntax

See [CostAnalysisMachining::CustomStockCostInfoType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~CustomStockCostInfoType.html).

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
