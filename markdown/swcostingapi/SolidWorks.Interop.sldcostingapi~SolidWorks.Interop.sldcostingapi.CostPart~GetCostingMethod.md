---
title: "GetCostingMethod Method (CostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "CostPart"
member: "GetCostingMethod"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart~GetCostingMethod.html"
---

# GetCostingMethod Method (CostPart)

Gets the manufacturing method for this Costing part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCostingMethod( _
   ByVal BodyName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostPart
Dim BodyName As System.String
Dim value As System.Integer

value = instance.GetCostingMethod(BodyName)
```

### C#

```csharp
System.int GetCostingMethod(
   System.string BodyName
)
```

### C++/CLI

```cpp
System.int GetCostingMethod(
   System.String^ BodyName
)
```

### Parameters

- `BodyName`: Name of the Costing body

### Return Value

Manufacturing method as specified in [swcMethodType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcMethodType_e.html)

## VBA Syntax

See [CostPart::GetCostingMethod](swcostingapivb6.chm::/SldCostingAPI~CostPart~GetCostingMethod.html).

## Remarks

For a [structural Costing analysis](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html), specify the name of the cut-list item for BodyName used for the manufacturing method.

## See Also

[CostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart.html)
[CostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
