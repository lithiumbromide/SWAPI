---
title: "MarkUpPercent Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "MarkUpPercent"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~MarkUpPercent.html"
---

# MarkUpPercent Property (ICostAnalysis)

Gets or sets the markup percentage for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MarkUpPercent As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Double

instance.MarkUpPercent = value

value = instance.MarkUpPercent
```

### C#

```csharp
System.double MarkUpPercent {get; set;}
```

### C++/CLI

```cpp
property System.double MarkUpPercent {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Markup percentage; valid range is -100 to +100; only valid when [ICostAnalysis::MarkUpType](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~MarkUpType.html) is not set to swcMarkUpType_e.swcMarkUpType_None

## VBA Syntax

See [CostAnalysis::MarkUpPercent](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~MarkUpPercent.html).

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
