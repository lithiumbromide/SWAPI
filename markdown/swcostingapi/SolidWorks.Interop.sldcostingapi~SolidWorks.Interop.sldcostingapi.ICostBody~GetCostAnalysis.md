---
title: "GetCostAnalysis Method (ICostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostBody"
member: "GetCostAnalysis"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~GetCostAnalysis.html"
---

# GetCostAnalysis Method (ICostBody)

Accesses the existing Cost analysis for this Costing body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCostAnalysis() As CostAnalysis
```

### Visual Basic (Usage)

```vb
Dim instance As ICostBody
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

Existing [Cost analysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis.html) for this Costing body

## VBA Syntax

See [CostBody::GetCostAnalysis](swcostingapivb6.chm::/SldCostingAPI~CostBody~GetCostAnalysis.html).

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## See Also

[ICostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody.html)
[ICostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody_members.html)
[ICostBody::CreateCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~CreateCostAnalysis.html)
[ICostPart::CreateCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~CreateCostAnalysis.html)
[ICostPart::GetCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostAnalysis.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
