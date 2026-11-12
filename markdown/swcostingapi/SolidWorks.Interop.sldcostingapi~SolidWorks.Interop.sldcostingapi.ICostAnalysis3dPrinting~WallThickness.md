---
title: "WallThickness Property (ICostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis3dPrinting"
member: "WallThickness"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~WallThickness.html"
---

# WallThickness Property (ICostAnalysis3dPrinting)

Gets or sets the wall thickness for this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property WallThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis3dPrinting
Dim value As System.Double

instance.WallThickness = value

value = instance.WallThickness
```

### C#

```csharp
System.double WallThickness {get; set;}
```

### C++/CLI

```cpp
property System.double WallThickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Wall thickness

## VBA Syntax

See [CostAnalysis3dPrinting::WallThickness](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~WallThickness.html).

## Examples

See the [ICostAnalysis3dPrinting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html) examples.

## See Also

[ICostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html)
[ICostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting_members.html)
[ICostAnalysis3dPrinting::PercentInfill Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~PercentInfill.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
