---
title: "GetFirstSubFeature Method (ICostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: "GetFirstSubFeature"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetFirstSubFeature.html"
---

# GetFirstSubFeature Method (ICostFeature)

Gets the first child feature that belongs to the Costing feature in the CostingManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstSubFeature() As CostFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
Dim value As CostFeature

value = instance.GetFirstSubFeature()
```

### C#

```csharp
CostFeature GetFirstSubFeature()
```

### C++/CLI

```cpp
CostFeature^ GetFirstSubFeature();
```

### Return Value

First [Costing child feature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature.html) or null if no Costing children features exist

## VBA Syntax

See [CostFeature::GetFirstSubFeature](swcostingapivb6.chm::/SldCostingAPI~CostFeature~GetFirstSubFeature.html).

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
[ICostFeature::GetNextFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetNextFeature.html)
[ICostFeature::GetNextSubFeature Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetNextSubFeature.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
