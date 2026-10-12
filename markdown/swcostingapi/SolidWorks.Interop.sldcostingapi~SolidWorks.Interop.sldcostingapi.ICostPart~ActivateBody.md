---
title: "ActivateBody Method (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "ActivateBody"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~ActivateBody.html"
---

# ActivateBody Method (ICostPart)

Activates the specified Costing body in the Costing part, which allows modifications to its Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateBody( _
   ByVal BodyName As System.String, _
   ByRef Errors As System.Integer _
) As CostBody
```

### Visual Basic (Usage)

```vb
Dim instance As ICostPart
Dim BodyName As System.String
Dim Errors As System.Integer
Dim value As CostBody

value = instance.ActivateBody(BodyName, Errors)
```

### C#

```csharp
CostBody ActivateBody(
   System.string BodyName,
   out System.int Errors
)
```

### C++/CLI

```cpp
CostBody^ ActivateBody(
   System.String^ BodyName,
   [Out] System.int Errors
)
```

### Parameters

- `BodyName`: Name of Costing body to activate or an empty string to activate the common [Cost analysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis.html) for this Costing part (see **Remarks**)
- `Errors`: Status as defined in [swcActivateBodyResult_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcActivateBodyResult_e.html)

### Return Value

[Costing body](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBody.html)

## VBA Syntax

See [CostPart::ActivateBody](swcostingapivb6.chm::/SldCostingAPI~CostPart~ActivateBody.html).

## Remarks

To get the name of a Costing body for BodyName:

1. Get the Costing bodies in the Costing part by calling:

1. Get the names of the Costing bodies in the Costing part by iterating through the array of returned Costing bodies and calling [ICostBody::GetName](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBody~GetName.html).

Activating Costing bodies by their names allows you to use names directly from existing references to [SOLIDWORKS bodies](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html).

If you passed an empty string to BodyName, then **Return Value** is null and Errors is swcActivateBodyResult_e.swcActivateBodyResult_Success.

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::ActiveBody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~ActiveBody.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
