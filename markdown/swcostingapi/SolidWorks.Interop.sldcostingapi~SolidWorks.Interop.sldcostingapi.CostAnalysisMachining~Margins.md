---
title: "Margins Property (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "Margins"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~Margins.html"
---

# Margins Property (CostAnalysisMachining)

Gets or sets the margins for the [stock type](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html) for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property Margins As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim value As System.Object

instance.Margins = value

value = instance.Margins
```

### C#

```csharp
System.object Margins {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Margins {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

Array of doubles of the margins for the stock type (see **Remarks**)

## VBA Syntax

See [CostAnalysisMachining::Margins](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~Margins.html).

## Remarks

The material determines the size of the array:

| Material | Array |
| --- | --- |
| Block | 6 doubles for the -X, +X, -Y, +Y, -Z, and +Z ICostAnalysisMachining::SpecificSizeEnabled must bet set to true to specify block dimensions to add to the tightest fitting stock faces. |
| Cylinder | 3 doubles for the -D, -L, and +L |
| Plate | 4 doubles, all 0, for the -W, +W, -L, and +L |

This property does not support setting margins:

- for plate material
  - or -
- when a [custom size](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~BlankSize.html) is defined.

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
