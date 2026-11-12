---
title: "GetSpecificAnalysis Method (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "GetSpecificAnalysis"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetSpecificAnalysis.html"
---

# GetSpecificAnalysis Method (ICostAnalysis)

Gets the specific Costing analysis in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSpecificAnalysis() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Object

value = instance.GetSpecificAnalysis()
```

### C#

```csharp
System.object GetSpecificAnalysis()
```

### C++/CLI

```cpp
System.Object^ GetSpecificAnalysis();
```

### Return Value

Specific Costing analysis of this type of the Costing part:

- [3D printing](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html)
- [Casting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
- [Machined](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining.html)
- [Plastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html)
- [Sheet metal](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
- [Structural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html)

## VBA Syntax

See [CostAnalysis::GetSpecificAnalysis](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~GetSpecificAnalysis.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## Remarks

A complete Costing analysis includes the common Costing analysis and a specific Costing analysis for either machining or sheet metal parts.

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
