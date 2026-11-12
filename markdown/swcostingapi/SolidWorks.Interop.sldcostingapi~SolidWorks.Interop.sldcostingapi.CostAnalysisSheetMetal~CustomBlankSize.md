---
title: "CustomBlankSize Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "CustomBlankSize"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~CustomBlankSize.html"
---

# CustomBlankSize Property (CostAnalysisSheetMetal)

Gets or sets a custom blank of a sheet metal part in this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomBlankSize As CostBlankSize
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim value As CostBlankSize

instance.CustomBlankSize = value

value = instance.CustomBlankSize
```

### C#

```csharp
CostBlankSize CustomBlankSize {get; set;}
```

### C++/CLI

```cpp
property CostBlankSize^ CustomBlankSize {
   CostBlankSize^ get();
   void set (    CostBlankSize^ value);
}
```

### Property Value

[ICostBlankSize](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBlankSize.html)

## VBA Syntax

See [CostAnalysisSheetMetal::CustomBlankSize](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~CustomBlankSize.html).

## Remarks

[ICostAnalysisSheetMetal::BlankSizeType](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankSizeType.html) must be set to swcSheetMetalBlankSizeType_e.swcSheetMetalBlankSizeType_CustomSize to set the length or width of a custom blank.

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
