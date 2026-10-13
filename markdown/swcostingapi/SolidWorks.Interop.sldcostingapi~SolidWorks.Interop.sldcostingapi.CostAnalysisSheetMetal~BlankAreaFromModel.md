---
title: "BlankAreaFromModel Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "BlankAreaFromModel"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~BlankAreaFromModel.html"
---

# BlankAreaFromModel Property (CostAnalysisSheetMetal)

Gets the area of a blank, excluding any [margin](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankOffset.html), from the sheet metal part for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BlankAreaFromModel As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim value As System.Double

value = instance.BlankAreaFromModel
```

### C#

```csharp
System.double BlankAreaFromModel {get;}
```

### C++/CLI

```cpp
property System.double BlankAreaFromModel {
   System.double get();
}
```

### Property Value

Area of the blank from the sheet metal part, excluding any margin

## VBA Syntax

See [CostAnalysisSheetMetal::BlankAreaFromModel](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~BlankAreaFromModel.html).

## Remarks

Use [ICostAnalysisSheetMetal::FinalAreaFromModel](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~FinalAreaFromModel.html) to get the area of a blank, including any margin, from a sheet metal part.

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
