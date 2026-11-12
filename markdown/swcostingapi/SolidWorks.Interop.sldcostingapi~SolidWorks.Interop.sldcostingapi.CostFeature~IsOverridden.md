---
title: "IsOverridden Property (CostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "CostFeature"
member: "IsOverridden"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature~IsOverridden.html"
---

# IsOverridden Property (CostFeature)

Gets whether a cost override was applied to this Costing feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsOverridden As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As CostFeature
Dim value As System.Boolean

value = instance.IsOverridden
```

### C#

```csharp
System.bool IsOverridden {get;}
```

### C++/CLI

```cpp
property System.bool IsOverridden {
   System.bool get();
}
```

### Property Value

True if a cost override was applied to this Costing feature, false if not

## VBA Syntax

See [CostFeature::IsOverridden](swcostingapivb6.chm::/SldCostingAPI~CostFeature~IsOverridden.html).

## See Also

[CostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature.html)
[CostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
