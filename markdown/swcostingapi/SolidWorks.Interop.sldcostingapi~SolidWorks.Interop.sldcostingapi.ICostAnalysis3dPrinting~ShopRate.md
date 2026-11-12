---
title: "ShopRate Property (ICostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis3dPrinting"
member: "ShopRate"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~ShopRate.html"
---

# ShopRate Property (ICostAnalysis3dPrinting)

Gets or sets the hourly shop rate for this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShopRate As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis3dPrinting
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

See [CostAnalysis3dPrinting::ShopRate](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~ShopRate.html).

## Examples

See the [ICostAnalysis3dPrinting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html) examples.

## See Also

[ICostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html)
[ICostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting_members.html)
[ICostAnalysis3dPrinting::ResetShopRate Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~ShopRate.html)
[ICostAnalysis3dPrinting::ShopRateApplied Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~ShopRateApplied.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
