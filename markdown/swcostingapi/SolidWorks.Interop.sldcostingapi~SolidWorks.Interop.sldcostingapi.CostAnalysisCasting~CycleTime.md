---
title: "CycleTime Property (CostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisCasting"
member: "CycleTime"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting~CycleTime.html"
---

# CycleTime Property (CostAnalysisCasting)

Gets or sets the casting process cycle time in hours for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CycleTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisCasting
Dim value As System.Double

instance.CycleTime = value

value = instance.CycleTime
```

### C#

```csharp
System.double CycleTime {get; set;}
```

### C++/CLI

```cpp
property System.double CycleTime {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Casting process cycle time in hours

## VBA Syntax

See [CostAnalysisCasting::CycleTime](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisCasting~CycleTime.html).

## Examples

See the [ICostAnalysisCasting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html) examples.

## See Also

[CostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting.html)
[CostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisCasting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
