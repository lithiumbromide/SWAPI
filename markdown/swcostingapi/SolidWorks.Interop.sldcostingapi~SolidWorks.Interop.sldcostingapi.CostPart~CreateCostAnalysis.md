---
title: "CreateCostAnalysis Method (CostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "CostPart"
member: "CreateCostAnalysis"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart~CreateCostAnalysis.html"
---

# CreateCostAnalysis Method (CostPart)

Creates a new Costing analysis for this Costing part using the specified Costing template.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCostAnalysis( _
   ByVal TemplatePath As System.String _
) As CostAnalysis
```

### Visual Basic (Usage)

```vb
Dim instance As CostPart
Dim TemplatePath As System.String
Dim value As CostAnalysis

value = instance.CreateCostAnalysis(TemplatePath)
```

### C#

```csharp
CostAnalysis CreateCostAnalysis(
   System.string TemplatePath
)
```

### C++/CLI

```cpp
CostAnalysis^ CreateCostAnalysis(
   System.String^ TemplatePath
)
```

### Parameters

- `TemplatePath`: Path and filename of the Costing template

### Return Value

New [Costing analysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis.html)

## VBA Syntax

See [CostPart::CreateCostAnalysis](swcostingapivb6.chm::/SldCostingAPI~CostPart~CreateCostAnalysis.html).

## Remarks

Any previous Costing analysis for this Costing part is replaced by this Costing analysis.

## See Also

[CostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart.html)
[CostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
