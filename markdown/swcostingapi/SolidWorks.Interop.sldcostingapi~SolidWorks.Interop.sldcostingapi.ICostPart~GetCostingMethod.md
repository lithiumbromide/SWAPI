---
title: "GetCostingMethod Method (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "GetCostingMethod"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html"
---

# GetCostingMethod Method (ICostPart)

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
Dim instance As ICostPart
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

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

For a [structural Costing analysis](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html), specify the name of the cut-list item for BodyName used for the manufacturing method.

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::SetCostingMethod Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~SetCostingMethod.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
