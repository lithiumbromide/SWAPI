---
title: "LotSize Property (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "LotSize"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~LotSize.html"
---

# LotSize Property (CostAnalysis)

Gets or sets the quantity of parts to produce per batch for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property LotSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.Integer

instance.LotSize = value

value = instance.LotSize
```

### C#

```csharp
System.int LotSize {get; set;}
```

### C++/CLI

```cpp
property System.int LotSize {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Quantity of parts to produce per batch

## VBA Syntax

See [CostAnalysis::LotSize](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~LotSize.html).

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
