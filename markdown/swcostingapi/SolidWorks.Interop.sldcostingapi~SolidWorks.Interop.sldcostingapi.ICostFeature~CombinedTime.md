---
title: "CombinedTime Property (ICostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: "CombinedTime"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~CombinedTime.html"
---

# CombinedTime Property (ICostFeature)

Gets or sets the time for this Costing feature or operation, including the combined times of Costing child features and operations.

## Syntax

### Visual Basic (Declaration)

```vb
Property CombinedTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
Dim value As System.Double

instance.CombinedTime = value

value = instance.CombinedTime
```

### C#

```csharp
System.double CombinedTime {get; set;}
```

### C++/CLI

```cpp
property System.double CombinedTime {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Time for this Costing feature or operation, including the combined times of Costing child features and operations

## VBA Syntax

See [CostFeature::CombinedTime](swcostingapivb6.chm::/SldCostingAPI~CostFeature~CombinedTime.html).

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
- ignored if the Costing feature disallows applying a cost override. For example, sheet metal Costing features must always return a time of 0; thus, times for sheet metal Costing features cannot be overridden.

## See Also

[ICostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html)
[ICostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature_members.html)
[ICostFeature::CombinedCost Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~CombinedCost.html)
[ICostFeature::IsOverridden Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~IsOverridden.html)
[ICostFeature::RemoveOverrideCostTime Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~RemoveOverrideCostTime.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
