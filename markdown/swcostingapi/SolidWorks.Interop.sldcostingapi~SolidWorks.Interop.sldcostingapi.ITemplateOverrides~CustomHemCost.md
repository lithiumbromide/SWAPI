---
title: "CustomHemCost Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "CustomHemCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~CustomHemCost.html"
---

# CustomHemCost Property (ITemplateOverrides)

Gets or sets the custom hem cost for sheet metal parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomHemCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
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

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

Setting this property is only applied if:

- [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is swcMethodType_e.swcMethodType_Sheetmetal.
- [ITemplateOverrides::UseCustomHemCost](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseCustomHemCost.html) is true.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
