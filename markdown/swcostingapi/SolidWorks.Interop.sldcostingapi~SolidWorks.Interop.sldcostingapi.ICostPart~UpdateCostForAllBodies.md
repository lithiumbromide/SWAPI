---
title: "UpdateCostForAllBodies Method (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "UpdateCostForAllBodies"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~UpdateCostForAllBodies.html"
---

# UpdateCostForAllBodies Method (ICostPart)

Updates the Costing data for all of the bodies in this Costing Part.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateCostForAllBodies() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostPart
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

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::IUpdateCostForAllBodies Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~IUpdateCostForAllBodies.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
