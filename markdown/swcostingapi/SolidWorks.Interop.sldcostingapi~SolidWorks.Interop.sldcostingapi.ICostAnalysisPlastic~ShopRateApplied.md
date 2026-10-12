---
title: "ShopRateApplied Property (ICostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisPlastic"
member: "ShopRateApplied"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~ShopRateApplied.html"
---

# ShopRateApplied Property (ICostAnalysisPlastic)

Gets or sets whether an [hourly shop rate](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~ShopRate.html) is applied to this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShopRateApplied As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisPlastic
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

[ICostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html)
[ICostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic_members.html)
[ICostAnalysisPlastic::ResetShopRate Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~ResetShopRate.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
