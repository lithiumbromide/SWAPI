---
title: "SlotFeatureRecognitionType Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "SlotFeatureRecognitionType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SlotFeatureRecognitionType.html"
---

# SlotFeatureRecognitionType Property (ITemplateOverrides)

Gets or sets the slot feature recognition option for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property SlotFeatureRecognitionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
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

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::ShowUndeterminedSlotsInNCAFolder Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~ShowUndeterminedSlotsInNCAFolder.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
