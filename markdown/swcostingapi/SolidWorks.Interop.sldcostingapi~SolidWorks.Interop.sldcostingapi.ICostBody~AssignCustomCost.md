---
title: "AssignCustomCost Method (ICostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostBody"
member: "AssignCustomCost"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~AssignCustomCost.html"
---

# AssignCustomCost Method (ICostBody)

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
Dim instance As ICostBody
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

[ICostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody.html)
[ICostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody_members.html)
[ICostAnalysis::GetSetupCost Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetSetupCost.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
