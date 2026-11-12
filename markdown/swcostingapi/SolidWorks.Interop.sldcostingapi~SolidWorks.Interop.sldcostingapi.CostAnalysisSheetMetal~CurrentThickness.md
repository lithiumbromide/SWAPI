---
title: "CurrentThickness Property (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "CurrentThickness"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~CurrentThickness.html"
---

# CurrentThickness Property (CostAnalysisSheetMetal)

Gets or sets the sheet metal thickness for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim value As System.Double

instance.CurrentThickness = value

value = instance.CurrentThickness
```

### C#

```csharp
System.double CurrentThickness {get; set;}
```

### C++/CLI

```cpp
property System.double CurrentThickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Sheet metal thickness

## VBA Syntax

See [CostAnalysisSheetMetal::CurrentThickness](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~CurrentThickness.html).

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
