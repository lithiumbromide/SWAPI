---
title: "FinishingOffset Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "FinishingOffset"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~FinishingOffset.html"
---

# FinishingOffset Property (TemplateOverrides)

Gets or sets the finishing offset for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property FinishingOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
Dim value As System.Double

instance.FinishingOffset = value

value = instance.FinishingOffset
```

### C#

```csharp
System.double FinishingOffset {get; set;}
```

### C++/CLI

```cpp
property System.double FinishingOffset {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Finishing offset for machined parts

## VBA Syntax

See [TemplateOverrides::FinishingOffset](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~FinishingOffset.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
