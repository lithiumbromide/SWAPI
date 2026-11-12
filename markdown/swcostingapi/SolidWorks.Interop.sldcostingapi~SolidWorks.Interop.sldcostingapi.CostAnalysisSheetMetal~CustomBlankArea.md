---
title: "CustomBlankArea Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "CustomBlankArea"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~CustomBlankArea.html"
---

# CustomBlankArea Property (CostAnalysisSheetMetal)

Gets or sets the area of a custom blank for a sheet metal part for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomBlankArea As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
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

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
