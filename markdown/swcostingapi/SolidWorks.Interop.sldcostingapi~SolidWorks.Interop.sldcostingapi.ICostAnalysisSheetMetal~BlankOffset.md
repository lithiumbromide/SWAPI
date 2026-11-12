---
title: "BlankOffset Property (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "BlankOffset"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankOffset.html"
---

# BlankOffset Property (ICostAnalysisSheetMetal)

Gets or sets the margin (also called offset) to use around the blank of the sheet metal part for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlankOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisSheetMetal
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

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::CustomBlankArea Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CustomBlankArea.html)
[ICostAnalysisSheetMetal::FinalAreaFromModel Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~FinalAreaFromModel.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
