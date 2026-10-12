---
title: "MoldCost Property (ICostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisCasting"
member: "MoldCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~MoldCost.html"
---

# MoldCost Property (ICostAnalysisCasting)

Gets or sets the cost of the mold for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MoldCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisCasting
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

[ICostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
[ICostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
