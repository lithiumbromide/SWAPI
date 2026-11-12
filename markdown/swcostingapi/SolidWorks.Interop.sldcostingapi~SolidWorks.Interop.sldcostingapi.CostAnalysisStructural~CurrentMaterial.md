---
title: "CurrentMaterial Property (CostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisStructural"
member: "CurrentMaterial"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural~CurrentMaterial.html"
---

# CurrentMaterial Property (CostAnalysisStructural)

Gets or sets the name of the material for this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterial As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisStructural
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

See [CostAnalysisStructural::CurrentMaterial](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~CurrentMaterial.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## Remarks

Setting this property could invalidate other settings, e.g., weldment stock profile, etc.

## See Also

[CostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural.html)
[CostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
