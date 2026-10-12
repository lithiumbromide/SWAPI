---
title: "CombinedCost Property (CostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "CostFeature"
member: "CombinedCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature~CombinedCost.html"
---

# CombinedCost Property (CostFeature)

Gets or sets the cost of this Costing feature or operation, including the combined cost of Costing child features and operations.

## Syntax

### Visual Basic (Declaration)

```vb
Property CombinedCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostFeature
Dim value As System.Double

instance.CombinedCost = value

value = instance.CombinedCost
```

### C#

```csharp
System.double CombinedCost {get; set;}
```

### C++/CLI

```cpp
property System.double CombinedCost {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Cost of this Costing feature or operation, including the combined cost of Costing child features and operations

## VBA Syntax

See [CostFeature::CombinedCost](swcostingapivb6.chm::/SldCostingAPI~CostFeature~CombinedCost.html).

## Remarks

Setting this property is:

- equivalent to applying a cost override to this Costing feature.
- ignored if the Costing feature disallows applying a cost override.

## See Also

[CostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature.html)
[CostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
