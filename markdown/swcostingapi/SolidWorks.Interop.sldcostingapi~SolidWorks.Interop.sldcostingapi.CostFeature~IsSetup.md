---
title: "IsSetup Property (CostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "CostFeature"
member: "IsSetup"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature~IsSetup.html"
---

# IsSetup Property (CostFeature)

Gets whether this Costing feature is a setup-related Costing feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsSetup As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As CostFeature
Dim value As System.Boolean

value = instance.IsSetup
```

### C#

```csharp
System.bool IsSetup {get;}
```

### C++/CLI

```cpp
property System.bool IsSetup {
   System.bool get();
}
```

### Property Value

True if this Costing feature is a setup-related Costing feature, false if not

## VBA Syntax

See [CostFeature::IsSetup](swcostingapivb6.chm::/SldCostingAPI~CostFeature~IsOverridden.html).

## See Also

[CostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature.html)
[CostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
