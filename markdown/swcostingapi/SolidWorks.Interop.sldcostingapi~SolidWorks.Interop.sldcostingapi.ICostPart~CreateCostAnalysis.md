---
title: "CreateCostAnalysis Method (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "CreateCostAnalysis"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~CreateCostAnalysis.html"
---

# CreateCostAnalysis Method (ICostPart)

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
Dim instance As ICostPart
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

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

Any previous Costing analysis for this Costing part is replaced by this Costing analysis.

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::GetCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostAnalysis.html)
[ICostBody::CreateCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~CreateCostAnalysis.html)
[ICostBody::GetCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~GetCostAnalysis.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
