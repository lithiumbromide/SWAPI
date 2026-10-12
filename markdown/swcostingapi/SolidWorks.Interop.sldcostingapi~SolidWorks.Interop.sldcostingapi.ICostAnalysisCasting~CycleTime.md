---
title: "CycleTime Property (ICostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisCasting"
member: "CycleTime"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~CycleTime.html"
---

# CycleTime Property (ICostAnalysisCasting)

Gets or sets the casting process cycle time in hours for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CycleTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisCasting
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

[ICostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
[ICostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
