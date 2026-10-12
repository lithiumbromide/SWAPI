---
title: "ShopRateApplied Property (CostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisPlastic"
member: "ShopRateApplied"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic~ShopRateApplied.html"
---

# ShopRateApplied Property (CostAnalysisPlastic)

Gets or sets whether an [hourly shop rate](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~ShopRate.html) is applied to this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShopRateApplied As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisPlastic
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

See [CostAnalysisPlastic::ShopRateApplied](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~ShopRateApplied.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## See Also

[CostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic.html)
[CostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
