---
title: "IncludeBody Method (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "IncludeBody"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~IncludeBody.html"
---

# IncludeBody Method (ICostPart)

Gets whether to include the specified Costing body in this Costing part in the Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IncludeBody( _
   ByVal BodyName As System.String, _
   ByVal Include As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostPart
Dim BodyName As System.String
Dim Include As System.Boolean
Dim value As System.Integer

value = instance.IncludeBody(BodyName, Include)
```

### C#

```csharp
System.int IncludeBody(
   System.string BodyName,
   System.bool Include
)
```

### C++/CLI

```cpp
System.int IncludeBody(
   System.String^ BodyName,
   System.bool Include
)
```

### Parameters

- `BodyName`: Name of the Costing body
- `Include`: True to include the Costing body in this Costing part in the Costing analysis, false to exclude the Costing body in this Costing part in the Costing analysis

### Return Value

Status as defined in [swcBodyStatus_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcBodyStatus_e.html)

## VBA Syntax

See [CostPart::IncludeBody](swcostingapivb6.chm::/SldCostingAPI~CostPart~IncludeBody.html).

## Remarks

To get the names of the Costing bodies in a Costing part:

1. Get the Costing bodies in the Costing part by calling:

1. Get the names of the Costing bodies in the Costing part by iterating through the array of returned Costing bodies and calling [ICostBody::GetName](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBody~GetName.html).

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::CreateCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~CreateCostAnalysis.html)
[ICostPart::GetCostAnalysis Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostAnalysis.html)
[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
