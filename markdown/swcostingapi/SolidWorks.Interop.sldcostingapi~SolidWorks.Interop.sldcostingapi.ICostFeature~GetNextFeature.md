---
title: "GetNextFeature Method (ICostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: "GetNextFeature"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetNextFeature.html"
---

# GetNextFeature Method (ICostFeature)

Gets the next Costing feature in the CostingManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextFeature() As CostFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
Dim value As CostFeature

value = instance.GetNextFeature()
```

### C#

```csharp
CostFeature GetNextFeature()
```

### C++/CLI

```cpp
CostFeature^ GetNextFeature();
```

### Return Value

Next [Costing feature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature.html) or null if no more Costing features exist

## VBA Syntax

See [CostFeature::GetNextFeature](swcostingapivb6.chm::/SldCostingAPI~CostFeature~GetNextFeature.html).

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
[ICostAnalysis::GetFirstCostFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~GetFirstCostFeature.html)
[ICostFeature::GetFirstSubFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetFirstSubFeature.html)
[ICostFeature::GetNextSubFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetNextSubFeature.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
