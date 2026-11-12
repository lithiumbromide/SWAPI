---
title: "SemiFinishingCostPerVolume Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "SemiFinishingCostPerVolume"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingCostPerVolume.html"
---

# SemiFinishingCostPerVolume Property (ITemplateOverrides)

Gets or sets the semi-finishing cost per volume for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property SemiFinishingCostPerVolume As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
Dim value As System.Double

instance.SemiFinishingCostPerVolume = value

value = instance.SemiFinishingCostPerVolume
```

### C#

```csharp
System.double SemiFinishingCostPerVolume {get; set;}
```

### C++/CLI

```cpp
property System.double SemiFinishingCostPerVolume {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Semi-finishing cost per volume for machined parts

## VBA Syntax

See [TemplateOverrides::SemiFinishingCostPerVolume](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~SemiFinishingCostPerVolume.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::SemiFinishingOffset Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingOffset.html)
[ITemplateOverrides::DefaultFinishingOperation Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~DefaultFinishingOperation.html)
[ITemplateOverrides::FinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingCostPerVolume.html)
[ITemplateOverrides::RoughingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~RoughingCostPerVolume.html)
[ITemplateOverrides::RoughingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~RoughingCostPerVolume.html)
[ITemplateOverrides::FinishingOffset Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingOffset.html)
[ITemplateOverrides::UseOffsetBasedFinishing Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseOffsetBasedFinishing.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
