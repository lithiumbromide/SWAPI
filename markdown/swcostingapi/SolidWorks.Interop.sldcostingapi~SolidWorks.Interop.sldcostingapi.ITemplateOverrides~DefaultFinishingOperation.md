---
title: "DefaultFinishingOperation Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "DefaultFinishingOperation"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~DefaultFinishingOperation.html"
---

# DefaultFinishingOperation Property (ITemplateOverrides)

Gets or sets the default finishing operation for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultFinishingOperation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
Dim value As System.Integer

instance.DefaultFinishingOperation = value

value = instance.DefaultFinishingOperation
```

### C#

```csharp
System.int DefaultFinishingOperation {get; set;}
```

### C++/CLI

```cpp
property System.int DefaultFinishingOperation {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Default finishing operation as defined in [swcFinishingOperationType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcFinishingOperationType_e.html)

## VBA Syntax

See [TemplateOverrides::DefaultFinishingOperation](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~DefaultFinishingOperation.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::FinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingCostPerVolume.html)
[ITemplateOverrides::SemiFinishingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingCostPerVolume.html)
[ITemplateOverrides::RoughingCostPerVolume Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~RoughingCostPerVolume.html)
[ITemplateOverrides::FinishingOffset Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~FinishingOffset.html)
[ITemplateOverrides::SemiFinishingOffset Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SemiFinishingOffset.html)
[ITemplateOverrides::UseOffsetBasedFinishing Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseOffsetBasedFinishing.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
