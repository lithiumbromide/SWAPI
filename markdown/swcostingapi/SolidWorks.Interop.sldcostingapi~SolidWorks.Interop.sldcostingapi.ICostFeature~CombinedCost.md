---
title: "CombinedCost Property (ICostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: "CombinedCost"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~CombinedCost.html"
---

# CombinedCost Property (ICostFeature)

Gets or sets the cost of this Costing feature or operation, including the combined cost of Costing child features and operations.

## Syntax

### Visual Basic (Declaration)

```vb
Property CombinedCost As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
Dim value As System.Double

instance.CombinedCost = value

value = instance.CombinedCost
```

### C#

```csharp
System.double CombinedCost {get; set;}
```

### C++/CLI

```cpp
property System.double CombinedCost {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Cost of this Costing feature or operation, including the combined cost of Costing child features and operations

## VBA Syntax

See [CostFeature::CombinedCost](swcostingapivb6.chm::/SldCostingAPI~CostFeature~CombinedCost.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## Remarks

Setting this property is:

- equivalent to applying a cost override to this Costing feature.
- ignored if the Costing feature disallows applying a cost override.

## See Also

[ICostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html)
[ICostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature_members.html)
[ICostFeature::CombinedTime Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~CombinedTime.html)
[ICostFeature::IsOverridden Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~IsOverridden.html)
[ICostFeature::RemoveOverrideCostTime Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~RemoveOverrideCostTime.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
