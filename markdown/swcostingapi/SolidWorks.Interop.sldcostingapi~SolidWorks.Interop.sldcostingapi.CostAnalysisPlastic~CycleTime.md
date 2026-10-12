---
title: "CycleTime Property (CostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisPlastic"
member: "CycleTime"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic~CycleTime.html"
---

# CycleTime Property (CostAnalysisPlastic)

Gets or sets the plastic process cycle time in hours for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CycleTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisPlastic
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

Plastic process cycle time in hours; valid for use in calculations only if [ICostAnalysisPlastic::CalculationMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~CalculationMethod.html) is set to swcMoldCalculationMethod_e.swcMoldCalculationMethod_CycleTime

## VBA Syntax

See [CostAnalysisPlastic::CycleTime](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~CycleTime.html).

## See Also

[CostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic.html)
[CostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisPlastic_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
