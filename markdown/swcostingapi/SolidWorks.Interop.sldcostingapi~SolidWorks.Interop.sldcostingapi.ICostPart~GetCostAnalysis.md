---
title: "GetCostAnalysis Method (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "GetCostAnalysis"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostAnalysis.html"
---

# GetCostAnalysis Method (ICostPart)

Accesses the existing Cost analysis for this Costing part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCostAnalysis() As CostAnalysis
```

### Visual Basic (Usage)

```vb
Dim instance As ICostPart
Dim value As CostAnalysis

value = instance.GetCostAnalysis()
```

### C#

```csharp
CostAnalysis GetCostAnalysis()
```

### C++/CLI

```cpp
CostAnalysis^ GetCostAnalysis();
```

### Return Value

Existing [Cost analysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis.html)

## VBA Syntax

See [CostPart::GetCostAnalysis](swcostingapivb6.chm::/SldCostingAPI~CostPart~GetCostAnalysis.html).

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::CreateCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~CreateCostAnalysis.html)
[ICostBody::GetCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~GetCostAnalysis.html)
[ICostBody::CreateCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~CreateCostAnalysis.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
