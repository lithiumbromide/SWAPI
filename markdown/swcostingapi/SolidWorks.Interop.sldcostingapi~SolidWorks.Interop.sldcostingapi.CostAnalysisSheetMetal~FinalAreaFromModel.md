---
title: "FinalAreaFromModel Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "FinalAreaFromModel"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~FinalAreaFromModel.html"
---

# FinalAreaFromModel Property (CostAnalysisSheetMetal)

Gets the area of a blank, including any [margin](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankOffset.html), from the sheet metal part for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FinalAreaFromModel As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim value As System.Double

value = instance.FinalAreaFromModel
```

### C#

```csharp
System.double FinalAreaFromModel {get;}
```

### C++/CLI

```cpp
property System.double FinalAreaFromModel {
   System.double get();
}
```

### Property Value

Area of the blank, including any margins, from the sheet metal part

## VBA Syntax

See [CostAnalysisSheetMetal::FinalAreaFromModel](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~FinalAreaFromModel.html).

## Remarks

Use [ICostAnalysisSheetMetal::BlankAreaFromModel](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankAreaFromModel.html) to get the area of a blank, excluding any margin, from a sheet metal part.

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
