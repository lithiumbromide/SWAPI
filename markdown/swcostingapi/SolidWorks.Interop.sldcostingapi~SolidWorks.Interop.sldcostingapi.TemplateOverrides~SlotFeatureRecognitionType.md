---
title: "SlotFeatureRecognitionType Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "SlotFeatureRecognitionType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~SlotFeatureRecognitionType.html"
---

# SlotFeatureRecognitionType Property (TemplateOverrides)

Gets or sets the slot feature recognition option for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property SlotFeatureRecognitionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
Dim value As System.Integer

instance.SlotFeatureRecognitionType = value

value = instance.SlotFeatureRecognitionType
```

### C#

```csharp
System.int SlotFeatureRecognitionType {get; set;}
```

### C++/CLI

```cpp
property System.int SlotFeatureRecognitionType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Slot feature recognition option as defined in [swcSlotFeatureRecognitionType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcSlotFeatureRecognitionType_e.html)

## VBA Syntax

See [TemplateOverrides::SlotFeatureRecognitionType](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~SlotFeatureRecognitionType.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
