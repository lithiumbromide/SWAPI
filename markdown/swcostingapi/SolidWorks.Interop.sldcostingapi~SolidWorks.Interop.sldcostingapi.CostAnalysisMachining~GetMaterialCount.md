---
title: "GetMaterialCount Method (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "GetMaterialCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~GetMaterialCount.html"
---

# GetMaterialCount Method (CostAnalysisMachining)

Gets the number of materials in the specified class from the Costing template for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialCount( _
   ByVal ClassName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim ClassName As System.String
Dim value As System.Integer

value = instance.GetMaterialCount(ClassName)
```

### C#

```csharp
System.int GetMaterialCount(
   System.string ClassName
)
```

### C++/CLI

```cpp
System.int GetMaterialCount(
   System.String^ ClassName
)
```

### Parameters

- `ClassName`: Name of material class

### Return Value

Number of materials in the specified class

## VBA Syntax

See [CostAnalysisMachining::GetMaterialCount](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~GetMaterialCount.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
