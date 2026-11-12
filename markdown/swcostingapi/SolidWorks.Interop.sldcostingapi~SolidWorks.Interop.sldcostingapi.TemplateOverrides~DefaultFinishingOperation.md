---
title: "DefaultFinishingOperation Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "DefaultFinishingOperation"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~DefaultFinishingOperation.html"
---

# DefaultFinishingOperation Property (TemplateOverrides)

Gets or sets the default finishing operation for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultFinishingOperation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
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

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
