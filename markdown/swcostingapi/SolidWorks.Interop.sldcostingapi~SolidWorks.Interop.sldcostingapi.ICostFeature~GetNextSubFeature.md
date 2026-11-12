---
title: "GetNextSubFeature Method (ICostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: "GetNextSubFeature"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetNextSubFeature.html"
---

# GetNextSubFeature Method (ICostFeature)

Gets the next Costing child feature from the owner of this Costing child feature in the CostingManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextSubFeature() As CostFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
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

[ICostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html)
[ICostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature_members.html)
[ICostAnalysis::GetFirstCostFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetFirstCostFeature.html)
[ICostFeature::GetFirstSubFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetFirstSubFeature.html)
[ICostFeature::GetNextFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetNextFeature.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
