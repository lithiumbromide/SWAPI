---
title: "FinishingCostPerVolume Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "FinishingCostPerVolume"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~FinishingCostPerVolume.html"
---

# FinishingCostPerVolume Property (TemplateOverrides)

Gets or sets the finishing cost per volume for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property FinishingCostPerVolume As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
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

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
