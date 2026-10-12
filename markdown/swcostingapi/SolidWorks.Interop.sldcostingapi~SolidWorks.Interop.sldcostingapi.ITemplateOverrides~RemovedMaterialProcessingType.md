---
title: "RemovedMaterialProcessingType Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "RemovedMaterialProcessingType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~RemovedMaterialProcessingType.html"
---

# RemovedMaterialProcessingType Property (ITemplateOverrides)

Gets or sets the removed material processing option for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property RemovedMaterialProcessingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
Dim value As System.Integer

instance.RemovedMaterialProcessingType = value

value = instance.RemovedMaterialProcessingType
```

### C#

```csharp
System.int RemovedMaterialProcessingType {get; set;}
```

### C++/CLI

```cpp
property System.int RemovedMaterialProcessingType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Removed material processing option as defined in [swcRemovedMaterialProcessingType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcRemovedMaterialProcessingType_e.html)

## VBA Syntax

See [TemplateOverrides::RemovedMaterialProcessingType](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~RemovedMaterialProcessingType.html).

## Remarks

Removed material can use either standard manufacturing process recognition or customizable volume feature recognition.

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
