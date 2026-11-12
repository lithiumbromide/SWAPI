---
title: "BodyStatus Property (CostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "CostBody"
member: "BodyStatus"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody~BodyStatus.html"
---

# BodyStatus Property (CostBody)

Gets the status of this Costing body.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BodyStatus As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostBody
Dim value As System.Integer

value = instance.BodyStatus
```

### C#

```csharp
System.int BodyStatus {get;}
```

### C++/CLI

```cpp
property System.int BodyStatus {
   System.int get();
}
```

### Property Value

Status of the Costing body as defined in [swcBodyStatus_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcBodyStatus_e.html)

## VBA Syntax

See [CostBody::BodyStatus](swcostingapivb6.chm::/SldCostingAPI~CostBody~BodyStatus.html).

## See Also

[CostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody.html)
[CostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
