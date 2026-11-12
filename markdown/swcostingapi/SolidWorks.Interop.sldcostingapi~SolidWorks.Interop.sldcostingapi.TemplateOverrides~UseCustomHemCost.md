---
title: "UseCustomHemCost Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "UseCustomHemCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~UseCustomHemCost.html"
---

# UseCustomHemCost Property (TemplateOverrides)

Gets or sets whether to use a [custom hem cost](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~CustomHemCost.html) for sheet metal parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseCustomHemCost As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
Dim value As System.Boolean

instance.UseCustomHemCost = value

value = instance.UseCustomHemCost
```

### C#

```csharp
System.bool UseCustomHemCost {get; set;}
```

### C++/CLI

```cpp
property System.bool UseCustomHemCost {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to use a custom hem cost for sheet metal parts, false to not

## VBA Syntax

See [TemplateOverrides::UseCustomHemCost](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~UseCustomHemCost.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is swcMethodType_e.swcMethodType_Sheetmetal.

## See Also

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
