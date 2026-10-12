---
title: "CustomBlankSize Property (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "CustomBlankSize"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CustomBlankSize.html"
---

# CustomBlankSize Property (ICostAnalysisSheetMetal)

Gets or sets a custom blank of a sheet metal part in this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomBlankSize As CostBlankSize
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisSheetMetal
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

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::CustomBlankArea Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CustomBlankArea.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
