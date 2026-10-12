---
title: "ICostAnalysis Interface"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: ""
kind: "interface"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html"
---

# ICostAnalysis Interface

Allows access to the common Costing analysis.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICostAnalysis
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
```

### C#

```csharp
public interface ICostAnalysis
```

### C++/CLI

```cpp
public interface class ICostAnalysis
```

## VBA Syntax

See [CostAnalysis](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## Remarks

A complete Costing analysis includes the common Costing analysis and a specific Costing analysis.

| Access... | For the specific Costing analysis of... |
| --- | --- |
| ICostAnalysis3dPrinting | Additive 3D printing process |
| ICostAnalysisCasting | Casting process |
| ICostAnalysisMachining | Part machined from solid block and plate stock material |
| ICostAnalysisPlastic | Additive injection-molded process |
| ICostAnalysisSheetMetal | Part that contains sheet metal features such as flanges, bends, or forming tools |
| ICostAnalysisStructural | Weldment structure |

## Accessors

[ICostBody::CreateCostAnalysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBody~CreateCostAnalysis.html)

[ICostBody::GetCostAnalysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBody~GetCostAnalysis.html)

[ICostPart::CreateCostAnalysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostPart~CreateCostAnalysis.html)

[ICostPart::GetCostAnalysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostPart~GetCostAnalysis.html)

## See Also

[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
