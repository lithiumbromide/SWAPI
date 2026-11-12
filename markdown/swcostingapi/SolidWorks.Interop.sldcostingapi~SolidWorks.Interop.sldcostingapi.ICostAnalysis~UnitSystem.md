---
title: "UnitSystem Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "UnitSystem"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~UnitSystem.html"
---

# UnitSystem Property (ICostAnalysis)

Gets the unit system from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UnitSystem As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Integer

value = instance.UnitSystem
```

### C#

```csharp
System.int UnitSystem {get;}
```

### C++/CLI

```cpp
property System.int UnitSystem {
   System.int get();
}
```

### Property Value

Unit system as defined in [swcUnitSystem_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcUnitSystem_e.html)

## VBA Syntax

See [CostAnalysis::UnitSystem](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~UnitSystem.html).

## Remarks

All output for all bodies in this Costing analysis are in these units.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
