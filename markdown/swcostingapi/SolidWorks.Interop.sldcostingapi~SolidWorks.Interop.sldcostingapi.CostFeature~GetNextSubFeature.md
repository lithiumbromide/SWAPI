---
title: "GetNextSubFeature Method (CostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "CostFeature"
member: "GetNextSubFeature"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature~GetNextSubFeature.html"
---

# GetNextSubFeature Method (CostFeature)

Gets the next Costing child feature from the owner of this Costing child feature in the CostingManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextSubFeature() As CostFeature
```

### Visual Basic (Usage)

```vb
Dim instance As CostFeature
Dim value As CostFeature

value = instance.GetNextSubFeature()
```

### C#

```csharp
CostFeature GetNextSubFeature()
```

### C++/CLI

```cpp
CostFeature^ GetNextSubFeature();
```

### Return Value

Next [Costing child feature of this Costing feature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature.html) or null if no more Costing children features for this Costing feature exist

## VBA Syntax

See [CostFeature::GetNextSubFeature](swcostingapivb6.chm::/SldCostingAPI~CostFeature~GetNextSubFeature.html).

## See Also

[CostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature.html)
[CostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
