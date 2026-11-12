---
title: "CurrentMaterialClass Property (CostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisStructural"
member: "CurrentMaterialClass"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural~CurrentMaterialClass.html"
---

# CurrentMaterialClass Property (CostAnalysisStructural)

Gets or sets the name of the material class for this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterialClass As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisStructural
Dim value As System.String

instance.CurrentMaterialClass = value

value = instance.CurrentMaterialClass
```

### C#

```csharp
System.string CurrentMaterialClass {get; set;}
```

### C++/CLI

```cpp
property System.String^ CurrentMaterialClass {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the material class

## VBA Syntax

See [CostAnalysisStructural::CurrentMaterialClass](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~CurrentMaterialClass.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## Remarks

Setting this property could invalidate other settings, e.g., material and weldment stock profile.

## See Also

[CostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural.html)
[CostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
