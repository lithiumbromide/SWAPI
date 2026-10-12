---
title: "SpecificSizeEnabled Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "SpecificSizeEnabled"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~SpecificSizeEnabled.html"
---

# SpecificSizeEnabled Property (ICostAnalysisMachining)

Gets or sets whether a user can specify the X, Y, and Z block dimensions to add to the tightest fitting stock faces for this machining Cost analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpecificSizeEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim value As System.Boolean

instance.SpecificSizeEnabled = value

value = instance.SpecificSizeEnabled
```

### C#

```csharp
System.bool SpecificSizeEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool SpecificSizeEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if a user can specify the X, Y, and Z block dimensions to add to the tightest fitting stock faces, false if not

## VBA Syntax

See [CostAnalysisMachining::SpecificSizeEnabled](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~SpecificSizeEnabled.html).

## Remarks

This property applies to block stock bodies only.

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::Margins Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~Margins.html)
[ICostAnalysisMachining::IMargins Property](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IMargins.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
