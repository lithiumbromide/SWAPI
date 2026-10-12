---
title: "MaterialCost Property (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "MaterialCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~MaterialCost.html"
---

# MaterialCost Property (ICostAnalysisSheetMetal)

Gets or sets the cost of the sheet metal material for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisSheetMetal
Dim value As System.Double

instance.MaterialCost = value

value = instance.MaterialCost
```

### C#

```csharp
System.double MaterialCost {get; set;}
```

### C++/CLI

```cpp
property System.double MaterialCost {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Cost of the sheet metal material

## VBA Syntax

See [CostAnalysisSheetMetal::MaterialCost](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~MaterialCost.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

To use the cost of the sheet metal material specified in the Costing template, use [ICostAnalysisSheetMetal::MaterialCostFromTemplate](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~MaterialCostFromTemplate.html).

## See Also

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::CurrentMaterial Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CurrentMaterial.html)
[ICostAnalysisSheetMetal::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetMaterials.html)
[ICostAnalysisSheetMetal::IGetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~IGetMaterials.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
