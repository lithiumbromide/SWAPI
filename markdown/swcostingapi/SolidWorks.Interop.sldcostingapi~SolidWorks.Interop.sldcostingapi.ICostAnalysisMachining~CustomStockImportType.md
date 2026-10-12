---
title: "CustomStockImportType Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "CustomStockImportType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockImportType.html"
---

# CustomStockImportType Property (ICostAnalysisMachining)

Gets and sets the custom stock import type for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomStockImportType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
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

## Examples

[Set Custom Stock Body in Machined Part (C#)](Set_Custom_Stock_Body_in_Machined_Part_Example_CSharp.htm)
[Set Custom Stock Body in Machined Part (VB.NET)](Set_Custom_Stock_Body_in_Machined_Part_Example_VBNET.htm)
[Set Custom Stock Body in Machined Part (VBA)](Set_Custom_Stock_Body_in_Machined%20Part_Example_VB.htm)

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::CurrentStockType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html)
[ICostAnalysisMachining::CustomStockBodyName Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockBodyName.html)
[ICostAnalysisMachining::CustomStockCostInfoType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockCostInfoType.html)
[ICostAnalysisMachining::CustomStockCustomCost Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockCustomCost.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
