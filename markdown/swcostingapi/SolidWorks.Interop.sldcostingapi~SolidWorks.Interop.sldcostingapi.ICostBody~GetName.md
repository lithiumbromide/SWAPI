---
title: "GetName Method (ICostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostBody"
member: "GetName"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~GetName.html"
---

# GetName Method (ICostBody)

Gets the name of the Costing body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostBody
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

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

The name of the Costing body returned by this method matches the name of the body in the CostingManager and the FeatureManager design tree.

[Activating Costing bodies](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostPart~ActivateBody.html) by name allows you to use names directly from existing references to [SOLIDWORKS bodies](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html).

## See Also

[ICostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody.html)
[ICostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody_members.html)
[ICostBody::GetSWBody Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~GetSWBody.html)
[ICostPart::ActiveBody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~ActiveBody.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
