---
title: "LengthUnit Property (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "LengthUnit"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~LengthUnit.html"
---

# LengthUnit Property (CostAnalysis)

Gets the unit for the length from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LengthUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.Integer

value = instance.LengthUnit
```

### C#

```csharp
System.int LengthUnit {get;}
```

### C++/CLI

```cpp
property System.int LengthUnit {
   System.int get();
}
```

### Property Value

Unit for the length as defined in [swcLengthUnit_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcLengthUnit_e.html)

## VBA Syntax

See [CostAnalysis::LengthUnit](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~LengthUnit.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
