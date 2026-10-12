---
title: "CustomStockCostInfoType Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "CustomStockCostInfoType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockCostInfoType.html"
---

# CustomStockCostInfoType Property (ICostAnalysisMachining)

Gets or sets the type of custom stock cost for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomStockCostInfoType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
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

## Examples

[Set Custom Stock Body in Machined Part (C#)](Set_Custom_Stock_Body_in_Machined_Part_Example_CSharp.htm)
[Set Custom Stock Body in Machined Part (VB.NET)](Set_Custom_Stock_Body_in_Machined_Part_Example_VBNET.htm)
[Set Custom Stock Body in Machined Part (VBA)](Set_Custom_Stock_Body_in_Machined%20Part_Example_VB.htm)

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::CurrentStockType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html)
[ICostAnalysisMachining::CustomStockBodyName Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockBodyName.html)
[ICostAnalysisMachining::CustomStockCustomCost Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockCustomCost.html)
[ICostAnalysisMachining::CustomStockImportType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockImportType.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
