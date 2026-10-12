---
title: "CustomHemCost Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "CustomHemCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~CustomHemCost.html"
---

# CustomHemCost Property (TemplateOverrides)

Gets or sets the custom hem cost for sheet metal parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomHemCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
Dim value As System.Double

instance.CustomHemCost = value

value = instance.CustomHemCost
```

### C#

```csharp
System.double CustomHemCost {get; set;}
```

### C++/CLI

```cpp
property System.double CustomHemCost {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Custom hem cost for sheet metal parts

## VBA Syntax

See [TemplateOverrides::CustomHemCost](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~CustomHemCost.html).

## Remarks

Setting this property is only applied if:

- [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is swcMethodType_e.swcMethodType_Sheetmetal.
- [ITemplateOverrides::UseCustomHemCost](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseCustomHemCost.html) is true.

## See Also

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
