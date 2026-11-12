---
title: "GetFirstSubFeature Method (CostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "CostFeature"
member: "GetFirstSubFeature"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature~GetFirstSubFeature.html"
---

# GetFirstSubFeature Method (CostFeature)

Gets the first child feature that belongs to the Costing feature in the CostingManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstSubFeature() As CostFeature
```

### Visual Basic (Usage)

```vb
Dim instance As CostFeature
Dim value As CostFeature

value = instance.GetFirstSubFeature()
```

### C#

```csharp
CostFeature GetFirstSubFeature()
```

### C++/CLI

```cpp
CostFeature^ GetFirstSubFeature();
```

### Return Value

First [Costing child feature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature.html) or null if no Costing children features exist

## VBA Syntax

See [CostFeature::GetFirstSubFeature](swcostingapivb6.chm::/SldCostingAPI~CostFeature~GetFirstSubFeature.html).

## See Also

[CostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature.html)
[CostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostFeature_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
