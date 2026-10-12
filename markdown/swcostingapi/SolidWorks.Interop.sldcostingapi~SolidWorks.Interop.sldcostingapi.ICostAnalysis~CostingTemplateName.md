---
title: "CostingTemplateName Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "CostingTemplateName"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CostingTemplateName.html"
---

# CostingTemplateName Property (ICostAnalysis)

Gets the name of the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CostingTemplateName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
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

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[ICostManager::GetTemplateCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~GetTemplateCount.html)
[ICostManager::GetTemplatePathnames Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~GetTemplatePathnames.html)
[ICostManager::IGetTemplatePathnames Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~IGetTemplatePathnames.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
