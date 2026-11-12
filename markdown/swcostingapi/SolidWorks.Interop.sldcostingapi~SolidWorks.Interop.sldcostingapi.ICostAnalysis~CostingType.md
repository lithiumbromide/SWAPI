---
title: "CostingType Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "CostingType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CostingType.html"
---

# CostingType Property (ICostAnalysis)

Gets the Costing type from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CostingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
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

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
