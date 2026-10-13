---
title: "ShopRate Property (ICostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisCasting"
member: "ShopRate"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~ShopRate.html"
---

# ShopRate Property (ICostAnalysisCasting)

Gets or sets the hourly shop rate for this casting Costing Analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShopRate As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisCasting
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

See [CostAnalysisCasting::ShopRate](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisCasting~ShopRate.html).

## Examples

See the [ICostAnalysisCasting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html) examples.

## See Also

[ICostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
[ICostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting_members.html)
[ICostAnalysisCasting::ResetShopRate Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~ResetShopRate.html)
[ICostAnalysisCasting::ShopRateApplied Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~ShopRateApplied.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
