---
title: "CurrentMaterial Property (CostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis3dPrinting"
member: "CurrentMaterial"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting~CurrentMaterial.html"
---

# CurrentMaterial Property (CostAnalysis3dPrinting)

Gets or sets the name of the material for this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterial As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis3dPrinting
Dim value As System.String

instance.CurrentMaterial = value

value = instance.CurrentMaterial
```

### C#

```csharp
System.string CurrentMaterial {get; set;}
```

### C++/CLI

```cpp
property System.String^ CurrentMaterial {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the material

## VBA Syntax

See [CostAnalysis3dPrinting::CurrentMaterial](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~CurrentMaterial.html).

## Examples

See the [ICostAnalysis3dPrinting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html) examples.

## Remarks

Setting this property could invalidate other settings.

## See Also

[CostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting.html)
[CostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis3dPrinting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
