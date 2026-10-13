---
title: "SetCostingMethod Method (CostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "CostPart"
member: "SetCostingMethod"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart~SetCostingMethod.html"
---

# SetCostingMethod Method (CostPart)

Sets the manufacturing method for this Costing part.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCostingMethod( _
   ByVal BodyName As System.String, _
   ByVal MethodType As System.Integer _
) As CostBody
```

### Visual Basic (Usage)

```vb
Dim instance As CostPart
Dim BodyName As System.String
Dim MethodType As System.Integer
Dim value As CostBody

value = instance.SetCostingMethod(BodyName, MethodType)
```

### C#

```csharp
CostBody SetCostingMethod(
   System.string BodyName,
   System.int MethodType
)
```

### C++/CLI

```cpp
CostBody^ SetCostingMethod(
   System.String^ BodyName,
   System.int MethodType
)
```

### Parameters

- `BodyName`: Name of the Costing body (see **Remarks**)
- `MethodType`: Manufacturing type as defined in [swcMethodType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcMethodType_e.html)

### Return Value

[Costing body](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody.html)

## VBA Syntax

See [CostPart::SetCostingMethod](swcostingapivb6.chm::/SldCostingAPI~CostPart~SetCostingMethod.html).

## Remarks

If you specify:

- a name for BodyName, then the current body is deleted and a new body of the type that you specified in MethodType is created. This method returns the newly created body and invalidates any previously selected bodies.
- an empty string for BodyName, then the body in a single body part or the currently selected body in a multibody part is used. This method returns this body.

For a [structural Costing analysis](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html), specify the name of the cut-list item for BodyName to use for the manufacturing method.

## See Also

[CostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart.html)
[CostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
