---
title: "GetBodyType Method (ICostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostBody"
member: "GetBodyType"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~GetBodyType.html"
---

# GetBodyType Method (ICostBody)

Gets the type of Costing body for the Costing analysis, which indicates which Costing template to use.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodyType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostBody
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

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## See Also

[ICostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody.html)
[ICostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
