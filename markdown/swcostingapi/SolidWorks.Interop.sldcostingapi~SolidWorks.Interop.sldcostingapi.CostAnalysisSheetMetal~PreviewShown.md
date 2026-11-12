---
title: "PreviewShown Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "PreviewShown"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~PreviewShown.html"
---

# PreviewShown Property (CostAnalysisSheetMetal)

Gets or sets whether to display a preview of the blank for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreviewShown As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim value As System.Boolean

instance.PreviewShown = value

value = instance.PreviewShown
```

### C#

```csharp
System.bool PreviewShown {get; set;}
```

### C++/CLI

```cpp
property System.bool PreviewShown {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to display a preview of the blank, false to not

## VBA Syntax

See [CostAnalysisSheetMetal::PreviewShown](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~PreviewShown.html).

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
