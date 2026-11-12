---
title: "LengthUnit Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "LengthUnit"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~LengthUnit.html"
---

# LengthUnit Property (ICostAnalysis)

Gets the unit for the length from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LengthUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
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

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
