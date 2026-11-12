---
title: "CustomStockBodyName Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "CustomStockBodyName"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockBodyName.html"
---

# CustomStockBodyName Property (ICostAnalysisMachining)

Gets or sets the name of the configuration or reference part for a custom stock body in a machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomStockBodyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
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

## Examples

[Set Custom Stock Body in Machined Part (C#)](Set_Custom_Stock_Body_in_Machined_Part_Example_CSharp.htm)
[Set Custom Stock Body in Machined Part (VB.NET)](Set_Custom_Stock_Body_in_Machined_Part_Example_VBNET.htm)
[Set Custom Stock Body in Machined Part (VBA)](Set_Custom_Stock_Body_in_Machined%20Part_Example_VB.htm)

## Remarks

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::CurrentStockType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html)
[ICostAnalysisMachining::CustomStockCostInfoType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockCostInfoType.html)
[ICostAnalysisMachining::CustomStockCustomCost Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CustomStockCustomCost.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
