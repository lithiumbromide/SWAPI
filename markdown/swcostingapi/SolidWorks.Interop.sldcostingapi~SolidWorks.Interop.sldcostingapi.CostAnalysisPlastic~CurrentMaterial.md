---
title: "CurrentMaterial Property (CostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisPlastic"
member: "CurrentMaterial"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic~CurrentMaterial.html"
---

# CurrentMaterial Property (CostAnalysisPlastic)

Gets or sets the name of the material for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterial As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisPlastic
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

See [CostAnalysisPlastic::CurrentMaterial](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~CurrentMaterial.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## Remarks

Setting this property could invalidate other settings.

## See Also

[CostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic.html)
[CostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
