---
title: "CustomStockBodyName Property (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "CustomStockBodyName"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~CustomStockBodyName.html"
---

# CustomStockBodyName Property (CostAnalysisMachining)

Gets or sets the name of the configuration or reference part for a custom stock body in a machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomStockBodyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim value As System.String

instance.CustomStockBodyName = value

value = instance.CustomStockBodyName
```

### C#

```csharp
System.string CustomStockBodyName {get; set;}
```

### C++/CLI

```cpp
property System.String^ CustomStockBodyName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

- Name of the configuration for a custom stock body; valid only if [ICostAnalysisMachining::CustomStockImportType](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockImportType.html) is set to swcCustomStockImportType_e.swcCustomStockImportType_Configuration and multiple configurations exist in the model

  - or -
- Path and file name of the reference part for a custom stock body; valid only if ICostAnalysisMachining::CustomStockImportType is set to swcCustomStockImportType_e.swcCustomStockImportType_ReferencePart

## VBA Syntax

See [CostAnalysisMachining::CustomStockBodyName](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~CustomStockBodyName.html).

## Remarks

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
