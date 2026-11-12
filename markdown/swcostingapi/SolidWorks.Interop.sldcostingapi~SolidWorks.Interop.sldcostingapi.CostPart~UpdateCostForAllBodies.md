---
title: "UpdateCostForAllBodies Method (CostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "CostPart"
member: "UpdateCostForAllBodies"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart~UpdateCostForAllBodies.html"
---

# UpdateCostForAllBodies Method (CostPart)

Updates the Costing data for all of the bodies in this Costing Part.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateCostForAllBodies() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostPart
Dim value As System.Object

value = instance.UpdateCostForAllBodies()
```

### C#

```csharp
System.object UpdateCostForAllBodies()
```

### C++/CLI

```cpp
System.Object^ UpdateCostForAllBodies();
```

### Return Value

Array of integers, or longs if using VBA, corresponding to each body in the part and indicating the Costing update status of that body as defined in [swcUpdateCostError_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcUpdateCostError_e.html)

## VBA Syntax

See [CostPart::UpdateCostForAllBodies](swcostingapivb6.chm::/SldCostingAPI~CostPart~UpdateCostForAllBodies.html).

## See Also

[CostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart.html)
[CostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
