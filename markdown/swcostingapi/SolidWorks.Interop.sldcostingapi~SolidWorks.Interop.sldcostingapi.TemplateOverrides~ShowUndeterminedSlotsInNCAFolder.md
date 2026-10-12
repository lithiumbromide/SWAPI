---
title: "ShowUndeterminedSlotsInNCAFolder Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "ShowUndeterminedSlotsInNCAFolder"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~ShowUndeterminedSlotsInNCAFolder.html"
---

# ShowUndeterminedSlotsInNCAFolder Property (TemplateOverrides)

Gets or sets whether slot features whose volume cannot be determined are displayed as items in the **No Cost Assigned** folder.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowUndeterminedSlotsInNCAFolder As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
Dim value As System.Boolean

instance.ShowUndeterminedSlotsInNCAFolder = value

value = instance.ShowUndeterminedSlotsInNCAFolder
```

### C#

```csharp
System.bool ShowUndeterminedSlotsInNCAFolder {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowUndeterminedSlotsInNCAFolder {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if features whose volume cannot be determined are displayed as items in the **No Cost Assigned** folder, false if not

## VBA Syntax

See [TemplateOverrides::ShowUndeterminedSlotsInNCAFolder](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~ShowUndeterminedSlotsInNCAFolder.html).

## Remarks

Setting this property is only applied if:

- [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.
- [ITemplateOverrides::SlotFeatureRecognitionType](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SlotFeatureRecognitionType.html) is swcSlotFeatureRecognitionType_e.swcSlotFeatureRecognitionType_Slot.

## See Also

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
