---
title: "UseOffsetBasedFinishing Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "UseOffsetBasedFinishing"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~UseOffsetBasedFinishing.html"
---

# UseOffsetBasedFinishing Property (TemplateOverrides)

Gets or sets the option to override template settings for offset-based finishing for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseOffsetBasedFinishing As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
Dim value As System.Boolean

instance.UseOffsetBasedFinishing = value

value = instance.UseOffsetBasedFinishing
```

### C#

```csharp
System.bool UseOffsetBasedFinishing {get; set;}
```

### C++/CLI

```cpp
property System.bool UseOffsetBasedFinishing {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to override template settings for offset-based finishing for machined parts, false to not

## VBA Syntax

See [TemplateOverrides::UseOffsetBasedFinishing](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~UseOffsetBasedFinishing.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
