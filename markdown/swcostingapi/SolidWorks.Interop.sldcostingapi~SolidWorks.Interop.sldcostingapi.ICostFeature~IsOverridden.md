---
title: "IsOverridden Property (ICostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: "IsOverridden"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~IsOverridden.html"
---

# IsOverridden Property (ICostFeature)

Gets whether a cost override was applied to this Costing feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsOverridden As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
Dim value As System.Boolean

value = instance.IsOverridden
```

### C#

```csharp
System.bool IsOverridden {get;}
```

### C++/CLI

```cpp
property System.bool IsOverridden {
   System.bool get();
}
```

### Property Value

True if a cost override was applied to this Costing feature, false if not

## VBA Syntax

See [CostFeature::IsOverridden](swcostingapivb6.chm::/SldCostingAPI~CostFeature~IsOverridden.html).

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
[ICostFeature::RemoveOverrideCostTime Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~RemoveOverrideCostTime.html)
[ICostFeature::CombinedCost Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~CombinedCost.html)
[ICostFeature::CombinedTime Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~CombinedTime.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
