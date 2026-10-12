---
title: "Length Property (CostBlankSize)"
project: "SOLIDWORKS Costing API Help"
interface: "CostBlankSize"
member: "Length"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBlankSize~Length.html"
---

# Length Property (CostBlankSize)

Gets or sets the length of a custom blank for a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Length As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostBlankSize
Dim value As System.Double

instance.Length = value

value = instance.Length
```

### C#

```csharp
System.double Length {get; set;}
```

### C++/CLI

```cpp
property System.double Length {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Length of a custom blank of a sheet metal part

## VBA Syntax

See [CostBlankSize::Length](swcostingapivb6.chm::/SldCostingAPI~CostBlankSize~Length.html).

## Remarks

[ICostAnalysisSheetMetal::BlankSizeType](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankSizeType.html) must be set to swcSheetMetalBlankSizeType_e.swcSheetMetalBlankSizeType_CustomSize to set the length or width of a custom blank.

## See Also

[CostBlankSize Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBlankSize.html)
[CostBlankSize Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBlankSize_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
