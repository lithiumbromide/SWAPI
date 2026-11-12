---
title: "CurrentStockUnitLength Property (ICostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisStructural"
member: "CurrentStockUnitLength"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentStockUnitLength.html"
---

# CurrentStockUnitLength Property (ICostAnalysisStructural)

Gets or sets the stock unit length for the weldment in this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentStockUnitLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisStructural
Dim value As System.Double

instance.CurrentStockUnitLength = value

value = instance.CurrentStockUnitLength
```

### C#

```csharp
System.double CurrentStockUnitLength {get; set;}
```

### C++/CLI

```cpp
property System.double CurrentStockUnitLength {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Stock unit size

## VBA Syntax

See [CostAnalysisStructural::CurrentStockUnitLength](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~CurrentStockUnitLength.html).

## Remarks

You must specify a value that matches a stock unit length value in the template. If you specify an invalid value, then a value closest to the structural member body length is used.

## See Also

[ICostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html)
[ICostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural_members.html)
[ICostAnalysisStructural::CurrentCostMethodType Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentCostMethodType.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
