---
title: "ShopRateApplied Property (ICostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisStructural"
member: "ShopRateApplied"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~ShopRateApplied.html"
---

# ShopRateApplied Property (ICostAnalysisStructural)

Gets or sets whether an [hourly shop rate](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~ShopRate.html) is applied to this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShopRateApplied As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisStructural
Dim value As System.Boolean

instance.ShopRateApplied = value

value = instance.ShopRateApplied
```

### C#

```csharp
System.bool ShopRateApplied {get; set;}
```

### C++/CLI

```cpp
property System.bool ShopRateApplied {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if an hourly shop rate is applied, false if not

## VBA Syntax

See [CostAnalysisStructural::ShopRateApplied](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~ShopRateApplied.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## See Also

[ICostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html)
[ICostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural_members.html)
[ICostAnalysisStructural::ResetShopRate Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~ResetShopRate.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
