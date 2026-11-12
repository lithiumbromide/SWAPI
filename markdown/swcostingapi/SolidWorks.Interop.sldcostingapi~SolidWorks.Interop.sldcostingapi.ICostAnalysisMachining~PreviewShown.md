---
title: "PreviewShown Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "PreviewShown"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~PreviewShown.html"
---

# PreviewShown Property (ICostAnalysisMachining)

Gets or sets whether to display a preview of the blank for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreviewShown As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim value As System.Boolean

instance.PreviewShown = value

value = instance.PreviewShown
```

### C#

```csharp
System.bool PreviewShown {get; set;}
```

### C++/CLI

```cpp
property System.bool PreviewShown {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to display a preview of the blank, false to not

## VBA Syntax

See [CostAnalysisMachining::PreviewShown](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~PreviewShown.html).

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
