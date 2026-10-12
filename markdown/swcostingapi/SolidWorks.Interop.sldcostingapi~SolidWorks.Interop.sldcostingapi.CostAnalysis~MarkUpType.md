---
title: "MarkUpType Property (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "MarkUpType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~MarkUpType.html"
---

# MarkUpType Property (CostAnalysis)

Gets or sets the method of markup for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MarkUpType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.Integer

instance.MarkUpType = value

value = instance.MarkUpType
```

### C#

```csharp
System.int MarkUpType {get; set;}
```

### C++/CLI

```cpp
property System.int MarkUpType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Method of markup as defined in [swcMarkUpType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcMarkUpType_e.html)

## VBA Syntax

See [CostAnalysis::MarkUpType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~MarkUpType.html).

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
