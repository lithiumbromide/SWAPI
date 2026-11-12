---
title: "FinishingOffset Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "FinishingOffset"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingOffset.html"
---

# FinishingOffset Property (ITemplateOverrides)

Gets or sets the finishing offset for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property FinishingOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
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

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::DefaultFinishingOperation Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~DefaultFinishingOperation.html)
[ITemplateOverrides::FinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingCostPerVolume.html)
[ITemplateOverrides::SemiFinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingCostPerVolume.html)
[ITemplateOverrides::SemiFinishingOffset Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingOffset.html)
[ITemplateOverrides::UseOffsetBasedFinishing Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseOffsetBasedFinishing.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
