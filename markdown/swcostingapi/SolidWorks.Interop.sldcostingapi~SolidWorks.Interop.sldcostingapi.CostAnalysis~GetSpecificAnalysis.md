---
title: "GetSpecificAnalysis Method (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "GetSpecificAnalysis"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~GetSpecificAnalysis.html"
---

# GetSpecificAnalysis Method (CostAnalysis)

Gets the specific Costing analysis in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSpecificAnalysis() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
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

## Remarks

A complete Costing analysis includes the common Costing analysis and a specific Costing analysis for either machining or sheet metal parts.

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
