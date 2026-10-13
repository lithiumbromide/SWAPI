---
title: "CostingTemplateName Property (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "CostingTemplateName"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~CostingTemplateName.html"
---

# CostingTemplateName Property (CostAnalysis)

Gets the name of the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CostingTemplateName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.String

value = instance.CostingTemplateName
```

### C#

```csharp
System.string CostingTemplateName {get;}
```

### C++/CLI

```cpp
property System.String^ CostingTemplateName {
   System.String^ get();
}
```

### Property Value

Name of the Costing template

## VBA Syntax

See [CostAnalysis::CostingTemplateName](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~CostingTemplateName.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
