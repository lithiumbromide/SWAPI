---
title: "RoughingCostPerVolume Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "RoughingCostPerVolume"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~RoughingCostPerVolume.html"
---

# RoughingCostPerVolume Property (TemplateOverrides)

Gets or sets the roughing cost per volume for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property RoughingCostPerVolume As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
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

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
