---
title: "BodyStatus Property (ICostBody)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostBody"
member: "BodyStatus"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody~BodyStatus.html"
---

# BodyStatus Property (ICostBody)

Gets the status of this Costing body.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BodyStatus As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostBody
Dim value As System.Integer

value = instance.BodyStatus
```

### C#

```csharp
System.int BodyStatus {get;}
```

### C++/CLI

```cpp
property System.int BodyStatus {
   System.int get();
}
```

### Property Value

Status of the Costing body as defined in [swcBodyStatus_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcBodyStatus_e.html)

## VBA Syntax

See [CostBody::BodyStatus](swcostingapivb6.chm::/SldCostingAPI~CostBody~BodyStatus.html).

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## See Also

[ICostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody.html)
[ICostBody Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody_members.html)
[ICostPart::IncludeBody Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~IncludeBody.html)
[ICostPart::ActivateBody Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~ActivateBody.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
