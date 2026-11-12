---
title: "BlankAreaFromModel Property (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "BlankAreaFromModel"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankAreaFromModel.html"
---

# BlankAreaFromModel Property (ICostAnalysisSheetMetal)

Gets the area of a blank, excluding any [margin](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankOffset.html), from the sheet metal part for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BlankAreaFromModel As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisSheetMetal
Dim value As System.Double

value = instance.BlankAreaFromModel
```

### C#

```csharp
System.double BlankAreaFromModel {get;}
```

### C++/CLI

```cpp
property System.double BlankAreaFromModel {
   System.double get();
}
```

### Property Value

Area of the blank from the sheet metal part, excluding any margin

## VBA Syntax

See [CostAnalysisSheetMetal::BlankAreaFromModel](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~BlankAreaFromModel.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

Use [ICostAnalysisSheetMetal::FinalAreaFromModel](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~FinalAreaFromModel.html) to get the area of a blank, including any margin, from a sheet metal part.

## See Also

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::CustomBlankArea Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CustomBlankArea.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
