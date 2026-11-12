---
title: "CostingType Property (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "CostingType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~CostingType.html"
---

# CostingType Property (CostAnalysis)

Gets the Costing type from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CostingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.Integer

value = instance.CostingType
```

### C#

```csharp
System.int CostingType {get;}
```

### C++/CLI

```cpp
property System.int CostingType {
   System.int get();
}
```

### Property Value

Costing type as defined in [swcCostType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcCostingType_e.html)

## VBA Syntax

See [CostAnalysis::CostingType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~CostingType.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
