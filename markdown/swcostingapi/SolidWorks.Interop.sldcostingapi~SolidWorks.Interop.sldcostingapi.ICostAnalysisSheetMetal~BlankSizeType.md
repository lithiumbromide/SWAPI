---
title: "BlankSizeType Property (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "BlankSizeType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankSizeType.html"
---

# BlankSizeType Property (ICostAnalysisSheetMetal)

Gets or sets the type of size of the blank for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlankSizeType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisSheetMetal
Dim value As System.Integer

instance.BlankSizeType = value

value = instance.BlankSizeType
```

### C#

```csharp
System.int BlankSizeType {get; set;}
```

### C++/CLI

```cpp
property System.int BlankSizeType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of size for the blank as defined in [swcSheetMetalBlankSizeType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcSheetMetalBlankSizeType_e.html)

## VBA Syntax

See [CostAnalysisSheetMetal::BlankSizeType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~BlankSizeType.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## See Also

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::BlankOffset Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankOffset.html)
[ICostAnalysisSheetMetal::CustomBlankArea Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CustomBlankArea.html)
[ICostAnalysisSheetMetal::CustomBlankSize Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CustomBlankSize.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
