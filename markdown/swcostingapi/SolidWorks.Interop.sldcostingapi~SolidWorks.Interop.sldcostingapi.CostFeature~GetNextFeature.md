---
title: "GetNextFeature Method (CostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "CostFeature"
member: "GetNextFeature"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature~GetNextFeature.html"
---

# GetNextFeature Method (CostFeature)

Gets the next Costing feature in the CostingManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextFeature() As CostFeature
```

### Visual Basic (Usage)

```vb
Dim instance As CostFeature
Dim value As CostFeature

value = instance.GetNextFeature()
```

### C#

```csharp
CostFeature GetNextFeature()
```

### C++/CLI

```cpp
CostFeature^ GetNextFeature();
```

### Return Value

Next [Costing feature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature.html) or null if no more Costing features exist

## VBA Syntax

See [CostFeature::GetNextFeature](swcostingapivb6.chm::/SldCostingAPI~CostFeature~GetNextFeature.html).

## See Also

[CostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature.html)
[CostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
