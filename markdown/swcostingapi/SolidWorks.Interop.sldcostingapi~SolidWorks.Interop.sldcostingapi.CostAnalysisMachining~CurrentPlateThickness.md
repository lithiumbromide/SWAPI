---
title: "CurrentPlateThickness Property (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "CurrentPlateThickness"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~CurrentPlateThickness.html"
---

# CurrentPlateThickness Property (CostAnalysisMachining)

Gets or sets the thickness of the plate for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentPlateThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim value As System.Double

instance.CurrentPlateThickness = value

value = instance.CurrentPlateThickness
```

### C#

```csharp
System.double CurrentPlateThickness {get; set;}
```

### C++/CLI

```cpp
property System.double CurrentPlateThickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Thickness of the plate

## VBA Syntax

See [CostAnalysisMachining::CurrentPlateThickness.](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~CurrentPlateThickness.html)

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
