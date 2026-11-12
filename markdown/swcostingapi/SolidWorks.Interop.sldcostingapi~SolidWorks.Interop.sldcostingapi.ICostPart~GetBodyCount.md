---
title: "GetBodyCount Method (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "GetBodyCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetBodyCount.html"
---

# GetBodyCount Method (ICostPart)

Gets the number of Costing bodies in this Costing part, including excluded and custom Costing bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodyCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostPart
Dim value As System.Integer

value = instance.GetBodyCount()
```

### C#

```csharp
System.int GetBodyCount()
```

### C++/CLI

```cpp
System.int GetBodyCount();
```

### Return Value

Number of Costing bodies

## VBA Syntax

See [CostPart::GetBodyCount](swcostingapivb6.chm::/SldCostingAPI~CostPart~GetBodyCount.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::IGetBodies](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~IGetBodies.html)
[ICostPart::GetBodies Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetBodies.html)
[ICostPart::IncludeBody Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~IncludeBody.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
