---
title: "CombinedTime Property (CostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "CostFeature"
member: "CombinedTime"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature~CombinedTime.html"
---

# CombinedTime Property (CostFeature)

Gets or sets the time for this Costing feature or operation, including the combined times of Costing child features and operations.

## Syntax

### Visual Basic (Declaration)

```vb
Property CombinedTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostFeature
Dim value As System.Double

instance.CombinedTime = value

value = instance.CombinedTime
```

### C#

```csharp
System.double CombinedTime {get; set;}
```

### C++/CLI

```cpp
property System.double CombinedTime {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Time for this Costing feature or operation, including the combined times of Costing child features and operations

## VBA Syntax

See [CostFeature::CombinedTime](swcostingapivb6.chm::/SldCostingAPI~CostFeature~CombinedTime.html).

## Remarks

Setting this property is:

- equivalent to applying a cost override to this Costing feature.
- ignored if the Costing feature disallows applying a cost override. For example, sheet metal Costing features must always return a time of 0; thus, times for sheet metal Costing features cannot be overridden.

## See Also

[CostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature.html)
[CostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
