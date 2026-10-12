---
title: "GetTemplatePathnames Method (ICostManager)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostManager"
member: "GetTemplatePathnames"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~GetTemplatePathnames.html"
---

# GetTemplatePathnames Method (ICostManager)

Gets the paths and filenames of the Costing templates available for the specified type of Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemplatePathnames( _
   ByVal CostingType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostManager
Dim CostingType As System.Integer
Dim value As System.Object

value = instance.GetTemplatePathnames(CostingType)
```

### C#

```csharp
System.object GetTemplatePathnames(
   System.int CostingType
)
```

### C++/CLI

```cpp
System.Object^ GetTemplatePathnames(
   System.int CostingType
)
```

### Parameters

- `CostingType`: Type of Costing analysis as defined in [swcCostingType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcCostingType_e.html)

### Return Value

Array of strings of the paths and filenames of the Costing templates available for CostingType

## VBA Syntax

See [CostManager::GetTemplatePathnames](swcostingapivb6.chm::/SldCostingAPI~CostManager~GetTemplatePathnames.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostManager Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager.html)
[ICostManager Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
