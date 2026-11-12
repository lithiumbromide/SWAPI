---
title: "CreateCostAnalysis Method (CostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "CostBody"
member: "CreateCostAnalysis"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody~CreateCostAnalysis.html"
---

# CreateCostAnalysis Method (CostBody)

Creates a new Costing analysis for this Costing body using the specified Costing template.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCostAnalysis( _
   ByVal TemplatePath As System.String _
) As CostAnalysis
```

### Visual Basic (Usage)

```vb
Dim instance As CostBody
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

New [Cost analysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis.html)

## VBA Syntax

See [CostBody::CreateCostAnalysis](swcostingapivb6.chm::/SldCostingAPI~CostBody~CreateCostAnalysis.html).

## Remarks

Any previous Costing analysis for this Costing body is replaced by this Costing analysis.

## See Also

[CostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody.html)
[CostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
