---
title: "UseCustomLibraryFeatureCost Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "UseCustomLibraryFeatureCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseCustomLibraryFeatureCost.html"
---

# UseCustomLibraryFeatureCost Property (ITemplateOverrides)

Gets or sets whether to use a [custom library feature cost](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~CustomLibraryFeatureCost.html) for sheet metal parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseCustomLibraryFeatureCost As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
Dim value As System.Boolean

instance.UseCustomLibraryFeatureCost = value

value = instance.UseCustomLibraryFeatureCost
```

### C#

```csharp
System.bool UseCustomLibraryFeatureCost {get; set;}
```

### C++/CLI

```cpp
property System.bool UseCustomLibraryFeatureCost {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to use a custom library feature cost for sheet metal parts, false to not

## VBA Syntax

See [TemplateOverrides::UseCustomLibraryFeatureCost](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~UseCustomLibraryFeatureCost.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is swcMethodType_e.swcMethodType_Sheetmetal.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
