---
title: "GetMaterialCount Method (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "GetMaterialCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~GetMaterialCount.html"
---

# GetMaterialCount Method (CostAnalysisSheetMetal)

Gets the number of materials in the specified class from the Costing template for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialCount( _
   ByVal ClassName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
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

See [CostAnalysisSheetMetal::GetMaterialCount](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~GetMaterialCount.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
