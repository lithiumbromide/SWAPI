---
title: "SemiFinishingOffset Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "SemiFinishingOffset"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~SemiFinishingOffset.html"
---

# SemiFinishingOffset Property (TemplateOverrides)

Gets or sets the semi-finishing offset for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property SemiFinishingOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
Dim value As System.Double

instance.SemiFinishingOffset = value

value = instance.SemiFinishingOffset
```

### C#

```csharp
System.double SemiFinishingOffset {get; set;}
```

### C++/CLI

```cpp
property System.double SemiFinishingOffset {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Semi-finishing offset for machined parts

## VBA Syntax

See [TemplateOverrides::SemiFinishingOffset](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~SemiFinishingOffset.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
