---
title: "SemiFinishingOffset Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "SemiFinishingOffset"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingOffset.html"
---

# SemiFinishingOffset Property (ITemplateOverrides)

Gets or sets the semi-finishing offset for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property SemiFinishingOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
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

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::SemiFinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingCostPerVolume.html)
[ITemplateOverrides::DefaultFinishingOperation Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~DefaultFinishingOperation.html)
[ITemplateOverrides::FinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingCostPerVolume.html)
[ITemplateOverrides::FinishingOffset Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingOffset.html)
[ITemplateOverrides::RoughingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~RoughingCostPerVolume.html)
[ITemplateOverrides::UseOffsetBasedFinishing Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseOffsetBasedFinishing.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
