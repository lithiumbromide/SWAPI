---
title: "ShopRate Property (CostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisStructural"
member: "ShopRate"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural~ShopRate.html"
---

# ShopRate Property (CostAnalysisStructural)

Gets or sets the hourly shop rate for this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShopRate As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisStructural
Dim value As System.Double

instance.ShopRate = value

value = instance.ShopRate
```

### C#

```csharp
System.double ShopRate {get; set;}
```

### C++/CLI

```cpp
property System.double ShopRate {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Hourly shop rate

## VBA Syntax

See [CostAnalysisStructural::ShopRate](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~ShopRate.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## See Also

[CostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural.html)
[CostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
