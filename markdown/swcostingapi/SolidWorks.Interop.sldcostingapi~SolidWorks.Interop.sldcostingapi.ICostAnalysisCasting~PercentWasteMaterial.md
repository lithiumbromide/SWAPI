---
title: "PercentWasteMaterial Property (ICostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisCasting"
member: "PercentWasteMaterial"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~PercentWasteMaterial.html"
---

# PercentWasteMaterial Property (ICostAnalysisCasting)

Gets or sets the percentage of waste material for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property PercentWasteMaterial As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisCasting
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

See [CostAnalysisCasting::PercentWasteMaterial](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisCasting~PercentWasteMaterial.html).

## Examples

See the [ICostAnalysisCasting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html) examples.

## See Also

[ICostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
[ICostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
