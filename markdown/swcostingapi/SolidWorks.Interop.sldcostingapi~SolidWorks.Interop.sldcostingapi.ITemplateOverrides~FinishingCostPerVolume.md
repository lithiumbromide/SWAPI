---
title: "FinishingCostPerVolume Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "FinishingCostPerVolume"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingCostPerVolume.html"
---

# FinishingCostPerVolume Property (ITemplateOverrides)

Gets or sets the finishing cost per volume for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property FinishingCostPerVolume As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
Dim value As System.Double

instance.FinishingCostPerVolume = value

value = instance.FinishingCostPerVolume
```

### C#

```csharp
System.double FinishingCostPerVolume {get; set;}
```

### C++/CLI

```cpp
property System.double FinishingCostPerVolume {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Finishing cost per volume for machined parts

## VBA Syntax

See [TemplateOverrides::FinishingCostPerVolume](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~FinishingCostPerVolume.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::DefaultFinishingOperation Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~DefaultFinishingOperation.html)
[ITemplateOverrides::FinishingOffset Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingOffset.html)
[ITemplateOverrides::SemiFinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingCostPerVolume.html)
[ITemplateOverrides::SemiFinishingOffset Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingOffset.html)
[ITemplateOverrides::UseOffsetBasedFinishing Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseOffsetBasedFinishing.html)
[ITemplateOverrides::RoughingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~RoughingCostPerVolume.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
