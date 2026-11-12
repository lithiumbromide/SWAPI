---
title: "CustomStockImportType Property (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "CustomStockImportType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~CustomStockImportType.html"
---

# CustomStockImportType Property (CostAnalysisMachining)

Gets and sets the custom stock import type for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomStockImportType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim value As System.Integer

instance.CustomStockImportType = value

value = instance.CustomStockImportType
```

### C#

```csharp
System.int CustomStockImportType {get; set;}
```

### C++/CLI

```cpp
property System.int CustomStockImportType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Custom stock import type as defined in [swcCustomStockImportType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcCustomStockImportType_e.html)

## VBA Syntax

See [CostAnalysisMachining::CustomStockImportType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~CustomStockImportType.html).

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
