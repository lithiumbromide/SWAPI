---
title: "PercentInfill Property (ICostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis3dPrinting"
member: "PercentInfill"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~PercentInfill.html"
---

# PercentInfill Property (ICostAnalysis3dPrinting)

Gets or sets the infill percentage for this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property PercentInfill As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis3dPrinting
Dim value As System.Double

instance.PercentInfill = value

value = instance.PercentInfill
```

### C#

```csharp
System.double PercentInfill {get; set;}
```

### C++/CLI

```cpp
property System.double PercentInfill {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Infill percentage; valid values are 0 through 100

## VBA Syntax

See [CostAnalysis3dPrinting::PercentInfill](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~PercentInfill.html).

## Examples

See the [ICostAnalysis3dPrinting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html) examples.

## See Also

[ICostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html)
[ICostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting_members.html)
[ICostAnalysis3dPrinting::WallThickness Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~WallThickness.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
