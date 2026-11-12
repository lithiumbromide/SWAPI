---
title: "GetBodies Method (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "GetBodies"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetBodies.html"
---

# GetBodies Method (ICostPart)

Gets the Costing bodies in this Costing part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodies() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostPart
Dim value As System.Object

value = instance.GetBodies()
```

### C#

```csharp
System.object GetBodies()
```

### C++/CLI

```cpp
System.Object^ GetBodies();
```

### Return Value

Array of [Costing bodies](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBody.html)

## VBA Syntax

See [CostPart::GetBodies](swcostingapivb6.chm::/SldCostingAPI~CostPart~GetBodies.html).

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::GetBodyCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetBodyCount.html)
[ICostPart::IGetBodies Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~IGetBodies.html)
[ICostPart::ActiveBody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~ActiveBody.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
