---
title: "SemiFinishingCostPerVolume Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "SemiFinishingCostPerVolume"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~SemiFinishingCostPerVolume.html"
---

# SemiFinishingCostPerVolume Property (TemplateOverrides)

Gets or sets the semi-finishing cost per volume for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property SemiFinishingCostPerVolume As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
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

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
