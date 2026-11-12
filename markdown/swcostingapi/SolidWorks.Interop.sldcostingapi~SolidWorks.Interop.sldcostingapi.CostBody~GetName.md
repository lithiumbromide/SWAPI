---
title: "GetName Method (CostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "CostBody"
member: "GetName"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody~GetName.html"
---

# GetName Method (CostBody)

Gets the name of the Costing body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostBody
Dim value As System.String

value = instance.GetName()
```

### C#

```csharp
System.string GetName()
```

### C++/CLI

```cpp
System.String^ GetName();
```

### Return Value

Name of the Costing body

## VBA Syntax

See [CostBody::GetName](swcostingapivb6.chm::/SldCostingAPI~CostBody~GetName.html).

## Remarks

The name of the Costing body returned by this method matches the name of the body in the CostingManager and the FeatureManager design tree.

[Activating Costing bodies](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostPart~ActivateBody.html) by name allows you to use names directly from existing references to [SOLIDWORKS bodies](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html).

## See Also

[CostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody.html)
[CostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostBody_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
