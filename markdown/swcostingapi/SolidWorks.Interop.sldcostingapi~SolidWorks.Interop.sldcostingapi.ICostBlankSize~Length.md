---
title: "Length Property (ICostBlankSize)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostBlankSize"
member: "Length"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBlankSize~Length.html"
---

# Length Property (ICostBlankSize)

Gets or sets the length of a custom blank for a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Length As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostBlankSize
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

[ICostBlankSize Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBlankSize.html)
[ICostBlankSize Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBlankSize_members.html)
[ICostBlankSize::Width Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBlankSize~Width.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
