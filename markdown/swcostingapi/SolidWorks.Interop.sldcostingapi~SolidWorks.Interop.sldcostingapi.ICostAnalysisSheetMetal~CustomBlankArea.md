---
title: "CustomBlankArea Property (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "CustomBlankArea"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CustomBlankArea.html"
---

# CustomBlankArea Property (ICostAnalysisSheetMetal)

Gets or sets the area of a custom blank for a sheet metal part for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomBlankArea As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisSheetMetal
Dim value As System.Double

instance.CustomBlankArea = value

value = instance.CustomBlankArea
```

### C#

```csharp
System.double CustomBlankArea {get; set;}
```

### C++/CLI

```cpp
property System.double CustomBlankArea {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Area of custom blank for a sheet metal part

## VBA Syntax

See [CostAnalysisSheetMetal::CustomBlankArea](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~CustomBlankArea.html).

## Remarks

[ICostAnalysisSheetMetal::BlankSizeType](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankSizeType.html) must be set to swcSheetMetalBlankSizeType_e.swcSheetMetalBlankSizeType_CustomArea to set the area of a custom blank.

## See Also

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::BlankAreaFromModel Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankAreaFromModel.html)
[ICostAnalysisSheetMetal::FinalAreaFromModel Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~FinalAreaFromModel.html)
[ICostAnalysisSheetMetal::CustomBlankSize Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CustomBlankSize.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
