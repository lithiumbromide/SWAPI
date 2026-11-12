---
title: "FlipDirection Property (ICostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis3dPrinting"
member: "FlipDirection"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~FlipDirection.html"
---

# FlipDirection Property (ICostAnalysis3dPrinting)

Gets or sets whether to flip the [printing direction](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~OrientationPlane.html) for this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis3dPrinting
Dim value As System.Boolean

instance.FlipDirection = value

value = instance.FlipDirection
```

### C#

```csharp
System.bool FlipDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipDirection {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to flip the printing direction, false to not

## VBA Syntax

See [CostAnalysis3dPrinting::FlipDirection](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~FlipDirection.html).

## See Also

[ICostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html)
[ICostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
