---
title: "MaterialCostFromTemplate Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "MaterialCostFromTemplate"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~MaterialCostFromTemplate.html"
---

# MaterialCostFromTemplate Property (CostAnalysisSheetMetal)

Gets the cost of the sheet metal material from the Costing template for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MaterialCostFromTemplate As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
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

## Remarks

To override the cost of the sheet metal material specified in the Costing template, use [ICostAnalysisSheetMetal::MaterialCost](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~MaterialCost.html).

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
