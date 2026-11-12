---
title: "RoughingCostPerVolume Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "RoughingCostPerVolume"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~RoughingCostPerVolume.html"
---

# RoughingCostPerVolume Property (ITemplateOverrides)

Gets or sets the roughing cost per volume for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property RoughingCostPerVolume As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
Dim value As System.Double

instance.RoughingCostPerVolume = value

value = instance.RoughingCostPerVolume
```

### C#

```csharp
System.double RoughingCostPerVolume {get; set;}
```

### C++/CLI

```cpp
property System.double RoughingCostPerVolume {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Roughing cost per volume for machined parts

## VBA Syntax

See [TemplateOverrides::RoughingCostPerVolume](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~RoughingCostPerVolume.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::DefaultFinishingOperation Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~DefaultFinishingOperation.html)
[ITemplateOverrides::FinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingCostPerVolume.html)
[ITemplateOverrides::SemiFinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingCostPerVolume.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
