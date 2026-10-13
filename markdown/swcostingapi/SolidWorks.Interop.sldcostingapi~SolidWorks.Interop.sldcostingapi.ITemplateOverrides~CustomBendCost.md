---
title: "CustomBendCost Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "CustomBendCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~CustomBendCost.html"
---

# CustomBendCost Property (ITemplateOverrides)

Gets or sets the custom cost per bend for sheet metal parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomBendCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
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

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

Setting this property is only applied if:

- [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is swcMethodType_e.swcMethodType_Sheetmetal.
- [ITemplateOverrides::UseCustomBendCost](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseCustomBendCost.html) is true.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
