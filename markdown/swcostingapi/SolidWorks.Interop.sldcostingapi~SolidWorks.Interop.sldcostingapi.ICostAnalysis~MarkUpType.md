---
title: "MarkUpType Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "MarkUpType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~MarkUpType.html"
---

# MarkUpType Property (ICostAnalysis)

Gets or sets the method of markup for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MarkUpType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Integer

instance.MarkUpType = value

value = instance.MarkUpType
```

### C#

```csharp
System.int MarkUpType {get; set;}
```

### C++/CLI

```cpp
property System.int MarkUpType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Method of markup as defined in [swcMarkUpType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcMarkUpType_e.html)

## VBA Syntax

See [CostAnalysis::MarkUpType](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~MarkUpType.html).

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[ICostAnalysis::MarkUpPercent Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~MarkUpPercent.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
