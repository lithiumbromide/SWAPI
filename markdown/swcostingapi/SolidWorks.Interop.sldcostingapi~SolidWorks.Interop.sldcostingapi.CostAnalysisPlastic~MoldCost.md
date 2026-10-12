---
title: "MoldCost Property (CostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisPlastic"
member: "MoldCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic~MoldCost.html"
---

# MoldCost Property (CostAnalysisPlastic)

Gets or sets the cost of the mold for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MoldCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisPlastic
Dim value As System.Double

instance.MoldCost = value

value = instance.MoldCost
```

### C#

```csharp
System.double MoldCost {get; set;}
```

### C++/CLI

```cpp
property System.double MoldCost {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Cost of the mold

## VBA Syntax

See [CostAnalysisPlastic::MoldCost](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~MoldCost.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## See Also

[CostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic.html)
[CostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
