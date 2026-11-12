---
title: "AssignCustomCost Method (CostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "CostBody"
member: "AssignCustomCost"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody~AssignCustomCost.html"
---

# AssignCustomCost Method (CostBody)

Sets the total cost (setup and operation) of a custom operation for this Costing body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AssignCustomCost( _
   ByVal fCost As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As CostBody
Dim fCost As System.Double

instance.AssignCustomCost(fCost)
```

### C#

```csharp
void AssignCustomCost(
   System.double fCost
)
```

### C++/CLI

```cpp
void AssignCustomCost(
   System.double fCost
)
```

### Parameters

- `fCost`: Total cost (setup and operation) of a custom operation

## VBA Syntax

See [CostBody::AssignCustomCost](swcostingapivb6.chm::/SldCostingAPI~CostBody~AssignCustomCost.html).

## See Also

[CostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody.html)
[CostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
