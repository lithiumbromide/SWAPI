---
title: "IUpdateCostForAllBodies Method (CostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "CostPart"
member: "IUpdateCostForAllBodies"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart~IUpdateCostForAllBodies.html"
---

# IUpdateCostForAllBodies Method (CostPart)

Updates the Costing data for all of the bodies in this Costing Part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IUpdateCostForAllBodies( _
   ByVal NumBodies As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostPart
Dim NumBodies As System.Integer
Dim value As System.Integer

value = instance.IUpdateCostForAllBodies(NumBodies)
```

### C#

```csharp
System.int IUpdateCostForAllBodies(
   System.int NumBodies
)
```

### C++/CLI

```cpp
System.int IUpdateCostForAllBodies(
   System.int NumBodies
)
```

### Parameters

- `NumBodies`: Number of bodies (see **Remarks**)

### Return Value

Array of integers, or longs if using VBA, corresponding to each body in the part and indicating the Costing update status of that body as defined in [swcUpdateCostError_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcUpdateCostError_e.html)

## VBA Syntax

See [CostPart::IUpdateCostForAllBodies](swcostingapivb6.chm::/SldCostingAPI~CostPart~IUpdateCostForAllBodies.html).

## Remarks

Before calling this method, call [ICostPart::GetBodyCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostPart~GetBodyCount.html) to get NumBodies.

## See Also

[CostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart.html)
[CostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
