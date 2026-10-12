---
title: "CurrentThickness Property (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "CurrentThickness"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CurrentThickness.html"
---

# CurrentThickness Property (ICostAnalysisSheetMetal)

Gets or sets the sheet metal thickness for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisSheetMetal
Dim value As System.Double

instance.CurrentThickness = value

value = instance.CurrentThickness
```

### C#

```csharp
System.double CurrentThickness {get; set;}
```

### C++/CLI

```cpp
property System.double CurrentThickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Sheet metal thickness

## VBA Syntax

See [CostAnalysisSheetMetal::CurrentThickness](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~CurrentThickness.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## See Also

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::GetModelThickness Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetModelThickness.html)
[ICostAnalysisSheetMetal::GetThicknesses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetThicknesses.html)
[ICostAnalysisSheetMetal::GetThicknessesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetThicknessesCount.html)
[ICostAnalysisSheetMetal::IGetThicknesses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~IGetThicknesses.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
