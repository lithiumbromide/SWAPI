---
title: "MaterialCost Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "MaterialCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~MaterialCost.html"
---

# MaterialCost Property (CostAnalysisSheetMetal)

Gets or sets the cost of the sheet metal material for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
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

## Remarks

To use the cost of the sheet metal material specified in the Costing template, use [ICostAnalysisSheetMetal::MaterialCostFromTemplate](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~MaterialCostFromTemplate.html).

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
