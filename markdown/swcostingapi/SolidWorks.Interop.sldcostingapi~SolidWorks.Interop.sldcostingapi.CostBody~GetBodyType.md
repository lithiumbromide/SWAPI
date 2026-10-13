---
title: "GetBodyType Method (CostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "CostBody"
member: "GetBodyType"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody~GetBodyType.html"
---

# GetBodyType Method (CostBody)

Gets the type of Costing body for the Costing analysis, which indicates which Costing template to use.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodyType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostBody
Dim value As System.Integer

value = instance.GetBodyType()
```

### C#

```csharp
System.int GetBodyType()
```

### C++/CLI

```cpp
System.int GetBodyType();
```

### Return Value

Type of Costing body as defined in [swcBodyType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcBodyType_e.html)

## VBA Syntax

See [CostBody::GetBodyType](swcostingapivb6.chm::/SldCostingAPI~CostBody~GetBodyType.html).

## See Also

[CostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody.html)
[CostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
