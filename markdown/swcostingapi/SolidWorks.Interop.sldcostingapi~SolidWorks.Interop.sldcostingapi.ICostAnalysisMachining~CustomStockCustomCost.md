---
title: "CustomStockCustomCost Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "CustomStockCustomCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockCustomCost.html"
---

# CustomStockCustomCost Property (ICostAnalysisMachining)

Gets or sets the custom stock cost for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomStockCustomCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim value As System.Double

instance.CustomStockCustomCost = value

value = instance.CustomStockCustomCost
```

### C#

```csharp
System.double CustomStockCustomCost {get; set;}
```

### C++/CLI

```cpp
property System.double CustomStockCustomCost {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Custom stock cost

## VBA Syntax

See [CostAnalysisMachining::CustomStockCustomCost](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~CustomStockCustomCost.html).

## Examples

[Set Custom Stock Body in Machined Part (C#)](Set_Custom_Stock_Body_in_Machined_Part_Example_CSharp.htm)
[Set Custom Stock Body in Machined Part (VB.NET)](Set_Custom_Stock_Body_in_Machined_Part_Example_VBNET.htm)
[Set Custom Stock Body in Machined Part (VBA)](Set_Custom_Stock_Body_in_Machined%20Part_Example_VB.htm)

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::CurrentStockType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html)
[ICostAnalysisMachining::CustomStockCostInfoType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockCostInfoType.html)
[ICostAnalysisMachining::CustomStockBodyName Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockBodyName.html)
[ICostAnalysisMachining::CustomStockImportType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockImportType.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
