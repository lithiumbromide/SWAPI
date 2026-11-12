---
title: "MoldCost Property (CostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisCasting"
member: "MoldCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting~MoldCost.html"
---

# MoldCost Property (CostAnalysisCasting)

Gets or sets the cost of the mold for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MoldCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisCasting
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

See [CostAnalysisCasting::MoldCost](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisCasting~MoldCost.html).

## Examples

See the [ICostAnalysisCasting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html) examples.

## See Also

[CostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting.html)
[CostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
