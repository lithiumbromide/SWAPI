---
title: "ActiveBody Property (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "ActiveBody"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~ActiveBody.html"
---

# ActiveBody Property (ICostPart)

Gets the active Costing body in this Costing part.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ActiveBody As CostBody
```

### Visual Basic (Usage)

```vb
Dim instance As ICostPart
Dim value As CostBody

value = instance.ActiveBody
```

### C#

```csharp
CostBody ActiveBody {get;}
```

### C++/CLI

```cpp
property CostBody^ ActiveBody {
   CostBody^ get();
}
```

### Property Value

Active [Costing body](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBody.html) or null if the common [Cost analysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis.html) is active

## VBA Syntax

See [CostPart::ActiveBody](swcostingapivb6.chm::/SldCostingAPI~CostPart~ActiveBody.html).

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::ActivateBody Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~ActivateBody.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
