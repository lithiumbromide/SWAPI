---
title: "BlankOffset Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "BlankOffset"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~BlankOffset.html"
---

# BlankOffset Property (CostAnalysisSheetMetal)

Gets or sets the margin (also called offset) to use around the blank of the sheet metal part for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlankOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim value As System.Double

instance.BlankOffset = value

value = instance.BlankOffset
```

### C#

```csharp
System.double BlankOffset {get; set;}
```

### C++/CLI

```cpp
property System.double BlankOffset {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Margin to use around the blank

## VBA Syntax

See [CostAnalysisSheetMetal::BlankOffset](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~BlankOffset.html).

## Remarks

[ICostAnalysisSheetMetal::BlankSizeType](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankSizeType.html) must be set to swcSheetMetalBlankSizeType_e.swcSheetMetalBlankSizeType_BoundingBox or swcSheetMetalBlankSizeType_e.swcSheetMetalBlankSizeType_FlatPattern to set a margin to use around the blank of this sheet metal part.

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
