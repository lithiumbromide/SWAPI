---
title: "TotalQuantity Property (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "TotalQuantity"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~TotalQuantity.html"
---

# TotalQuantity Property (CostAnalysis)

Gets or sets the total quantity of parts to produce for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property TotalQuantity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.Integer

instance.TotalQuantity = value

value = instance.TotalQuantity
```

### C#

```csharp
System.int TotalQuantity {get; set;}
```

### C++/CLI

```cpp
property System.int TotalQuantity {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Total quantity of parts to produce

## VBA Syntax

See [CostAnalysis::TotalQuantity](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~TotalQuantity.html).

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
