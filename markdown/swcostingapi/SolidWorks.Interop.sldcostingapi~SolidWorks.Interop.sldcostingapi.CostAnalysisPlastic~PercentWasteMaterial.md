---
title: "PercentWasteMaterial Property (CostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisPlastic"
member: "PercentWasteMaterial"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic~PercentWasteMaterial.html"
---

# PercentWasteMaterial Property (CostAnalysisPlastic)

Gets or sets the percentage of waste material for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property PercentWasteMaterial As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisPlastic
Dim value As System.Double

instance.PercentWasteMaterial = value

value = instance.PercentWasteMaterial
```

### C#

```csharp
System.double PercentWasteMaterial {get; set;}
```

### C++/CLI

```cpp
property System.double PercentWasteMaterial {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Percentage of waste material; valid values are 0 through 100

## VBA Syntax

See [CostAnalysisPlastic::PercentWasteMaterial](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~PercentWasteMaterial.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## See Also

[CostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic.html)
[CostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
