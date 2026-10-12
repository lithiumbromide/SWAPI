---
title: "OrientationPlane Property (CostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis3dPrinting"
member: "OrientationPlane"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting~OrientationPlane.html"
---

# OrientationPlane Property (CostAnalysis3dPrinting)

Gets or sets the printing direction for this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property OrientationPlane As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis3dPrinting
Dim value As System.Integer

instance.OrientationPlane = value

value = instance.OrientationPlane
```

### C#

```csharp
System.int OrientationPlane {get; set;}
```

### C++/CLI

```cpp
property System.int OrientationPlane {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Printing direction as defined in [swcPlane_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcPlane_e.html)

## VBA Syntax

See [CostAnalysis3dPrinting::OrientationPlane](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~OrientationPlane.html).

## Examples

See the [ICostAnalysis3dPrinting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html) examples.

## Remarks

To flip the printing direction, call [ICostAnalysis3dPrinting::FlipDirection](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~FlipDirection.html).

## See Also

[CostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting.html)
[CostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
