---
title: "BlankSizeType Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "BlankSizeType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~BlankSizeType.html"
---

# BlankSizeType Property (CostAnalysisSheetMetal)

Gets or sets the type of size of the blank for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlankSizeType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim value As System.Integer

instance.BlankSizeType = value

value = instance.BlankSizeType
```

### C#

```csharp
System.int BlankSizeType {get; set;}
```

### C++/CLI

```cpp
property System.int BlankSizeType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of size for the blank as defined in [swcSheetMetalBlankSizeType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcSheetMetalBlankSizeType_e.html)

## VBA Syntax

See [CostAnalysisSheetMetal::BlankSizeType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~BlankSizeType.html).

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
