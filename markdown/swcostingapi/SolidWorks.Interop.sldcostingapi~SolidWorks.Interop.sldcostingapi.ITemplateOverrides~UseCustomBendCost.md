---
title: "UseCustomBendCost Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "UseCustomBendCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseCustomBendCost.html"
---

# UseCustomBendCost Property (ITemplateOverrides)

Gets or sets whether to use a [custom cost per bend](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~CustomBendCost.html) for sheet metal parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseCustomBendCost As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
Dim value As System.Boolean

instance.UseCustomBendCost = value

value = instance.UseCustomBendCost
```

### C#

```csharp
System.bool UseCustomBendCost {get; set;}
```

### C++/CLI

```cpp
property System.bool UseCustomBendCost {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to use a custom cost per bend for sheet metal parts, false to not

## VBA Syntax

See [TemplateOverrides::UseCustomBendCost](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~UseCustomBendCost.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is swcMethodType_e.swcMethodType_Sheetmetal.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
