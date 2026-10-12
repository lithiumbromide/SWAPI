---
title: "MassUnit Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "MassUnit"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~MassUnit.html"
---

# MassUnit Property (ICostAnalysis)

Gets the unit of mass from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MassUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Integer

value = instance.MassUnit
```

### C#

```csharp
System.int MassUnit {get;}
```

### C++/CLI

```cpp
property System.int MassUnit {
   System.int get();
}
```

### Property Value

Unit of mass as defined in [swcMassUnit_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcMassUnit_e.html)

## VBA Syntax

See [CostAnalysis::MassUnit](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~MassUnit.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
