---
title: "GetTemplateCount Method (ICostManager)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostManager"
member: "GetTemplateCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~GetTemplateCount.html"
---

# GetTemplateCount Method (ICostManager)

Gets the number of Costing templates available for the specified type of Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemplateCount( _
   ByVal CostingType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostManager
Dim CostingType As System.Integer
Dim value As System.Integer

value = instance.GetTemplateCount(CostingType)
```

### C#

```csharp
System.int GetTemplateCount(
   System.int CostingType
)
```

### C++/CLI

```cpp
System.int GetTemplateCount(
   System.int CostingType
)
```

### Parameters

- `CostingType`: Type of Costing analysis as defined in [swcCostingType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcCostingType_e.html)

### Return Value

Number of Costing templates available for CostingType

## VBA Syntax

See [CostManager::GetTemplateCount](swcostingapivb6.chm::/SldCostingAPI~CostManager~GetTemplateCount.html).

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostManager Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager.html)
[ICostManager Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager_members.html)
[ICostManager::GetTemplatePathnames Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~GetTemplatePathnames.html)
[ICostManager::IGetTemplatePathnames Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~IGetTemplatePathnames.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
