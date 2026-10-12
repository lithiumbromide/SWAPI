---
title: "ShopRate Property (ICostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisPlastic"
member: "ShopRate"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~ShopRate.html"
---

# ShopRate Property (ICostAnalysisPlastic)

Gets or sets the hourly shop rate for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShopRate As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisPlastic
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

See [CostAnalysisPlastic::ShopRate](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~ShopRate.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## See Also

[ICostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html)
[ICostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic_members.html)
[ICostAnalysisPlastic::ResetShopRate Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~ResetShopRate.html)
[ICostAnalysisPlastic::ShopRateApplied Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~ShopRateApplied.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
