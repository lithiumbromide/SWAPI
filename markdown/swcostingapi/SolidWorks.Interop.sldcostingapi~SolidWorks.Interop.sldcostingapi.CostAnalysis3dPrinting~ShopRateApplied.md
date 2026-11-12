---
title: "ShopRateApplied Property (CostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis3dPrinting"
member: "ShopRateApplied"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting~ShopRateApplied.html"
---

# ShopRateApplied Property (CostAnalysis3dPrinting)

Gets or sets whether an [hourly shop rate](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~ShopRate.html) is applied to this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShopRateApplied As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis3dPrinting
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

See [CostAnalysis3dPrinting::ShopRateApplied](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~ShopRateApplied.html).

## Examples

See the [ICostAnalysis3dPrinting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html) examples.

## See Also

[CostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting.html)
[CostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
