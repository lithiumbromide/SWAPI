---
title: "CustomLibraryFeatureCost Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "CustomLibraryFeatureCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~CustomLibraryFeatureCost.html"
---

# CustomLibraryFeatureCost Property (ITemplateOverrides)

Gets or sets the custom library feature cost for sheet metal parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomLibraryFeatureCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
Dim value As System.Double

instance.CustomLibraryFeatureCost = value

value = instance.CustomLibraryFeatureCost
```

### C#

```csharp
System.double CustomLibraryFeatureCost {get; set;}
```

### C++/CLI

```cpp
property System.double CustomLibraryFeatureCost {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Custom library feature cost for sheet metal parts

## VBA Syntax

See [TemplateOverrides::CustomLibraryFeatureCost](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~CustomLibraryFeatureCost.html).

## Remarks

Setting this property is only applied if:

- [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is swcMethodType_e.swcMethodType_Sheetmetal.
- [ITemplateOverrides::UseCustomLibraryFeatureCost](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~UseCustomLibraryFeatureCost.html) is true.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
