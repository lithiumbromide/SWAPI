---
title: "Width Property (CostBlankSize)"
project: "SOLIDWORKS Costing API Help"
interface: "CostBlankSize"
member: "Width"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBlankSize~Width.html"
---

# Width Property (CostBlankSize)

Gets or sets the width of a custom blank of a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostBlankSize
Dim value As System.Double

instance.Width = value

value = instance.Width
```

### C#

```csharp
System.double Width {get; set;}
```

### C++/CLI

```cpp
property System.double Width {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Width of a custom blank of a sheet metal part

## VBA Syntax

See [CostBlankSize::Width](swcostingapivb6.chm::/SldCostingAPI~CostBlankSize~Length.html).

## Remarks

[ICostAnalysisSheetMetal::BlankSizeType](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankSizeType.html) must be set to swcSheetMetalBlankSizeType_e.swcSheetMetalBlankSizeType_CustomSize to set the length or width of a custom blank.

## See Also

[CostBlankSize Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBlankSize.html)
[CostBlankSize Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBlankSize_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
