---
title: "CustomBendCost Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "CustomBendCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~CustomBendCost.html"
---

# CustomBendCost Property (TemplateOverrides)

Gets or sets the custom cost per bend for sheet metal parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomBendCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
Dim value As System.Double

instance.CustomBendCost = value

value = instance.CustomBendCost
```

### C#

```csharp
System.double CustomBendCost {get; set;}
```

### C++/CLI

```cpp
property System.double CustomBendCost {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Custom cost per bend for sheet metal parts

## VBA Syntax

See [TemplateOverrides::CustomBendCost](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~CustomBendCost.html).

## Remarks

Setting this property is only applied if:

- [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is swcMethodType_e.swcMethodType_Sheetmetal.
- [ITemplateOverrides::UseCustomBendCost](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseCustomBendCost.html) is true.

## See Also

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
