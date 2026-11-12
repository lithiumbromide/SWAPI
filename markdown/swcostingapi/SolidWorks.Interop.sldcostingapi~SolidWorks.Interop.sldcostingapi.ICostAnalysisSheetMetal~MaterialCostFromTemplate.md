---
title: "MaterialCostFromTemplate Property (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "MaterialCostFromTemplate"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~MaterialCostFromTemplate.html"
---

# MaterialCostFromTemplate Property (ICostAnalysisSheetMetal)

Gets the cost of the sheet metal material from the Costing template for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MaterialCostFromTemplate As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisSheetMetal
Dim value As System.Double

value = instance.MaterialCostFromTemplate
```

### C#

```csharp
System.double MaterialCostFromTemplate {get;}
```

### C++/CLI

```cpp
property System.double MaterialCostFromTemplate {
   System.double get();
}
```

### Property Value

Cost of the sheet metal material from the Costing template

## VBA Syntax

See [CostAnalysisSheetMetal::MaterialCostFromTemplate](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~MaterialCostFromTemplate.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

To override the cost of the sheet metal material specified in the Costing template, use [ICostAnalysisSheetMetal::MaterialCost](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~MaterialCost.html).

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::CurrentMaterial Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CurrentMaterial.html)
[ICostAnalysisSheetMetal::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetMaterials.html)
[ICostAnalysisSheetMetal::IGetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~IGetMaterials.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
