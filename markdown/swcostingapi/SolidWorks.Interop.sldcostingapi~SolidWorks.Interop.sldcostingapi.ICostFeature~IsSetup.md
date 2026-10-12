---
title: "IsSetup Property (ICostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: "IsSetup"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~IsSetup.html"
---

# IsSetup Property (ICostFeature)

Gets whether this Costing feature is a setup-related Costing feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsSetup As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
Dim value As System.Boolean

value = instance.IsSetup
```

### C#

```csharp
System.bool IsSetup {get;}
```

### C++/CLI

```cpp
property System.bool IsSetup {
   System.bool get();
}
```

### Property Value

True if this Costing feature is a setup-related Costing feature, false if not

## VBA Syntax

See [CostFeature::IsSetup](swcostingapivb6.chm::/SldCostingAPI~CostFeature~IsOverridden.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## See Also

[ICostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html)
[ICostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
