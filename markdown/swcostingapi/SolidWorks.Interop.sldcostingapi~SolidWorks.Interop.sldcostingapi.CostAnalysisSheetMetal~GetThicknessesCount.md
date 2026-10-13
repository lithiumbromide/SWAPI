---
title: "GetThicknessesCount Method (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "GetThicknessesCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~GetThicknessesCount.html"
---

# GetThicknessesCount Method (CostAnalysisSheetMetal)

Gets the number of sheet metal thicknesses for the specified material from the Costing template for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThicknessesCount( _
   ByVal ClassName As System.String, _
   ByVal MaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim ClassName As System.String
Dim MaterialName As System.String
Dim value As System.Integer

value = instance.GetThicknessesCount(ClassName, MaterialName)
```

### C#

```csharp
System.int GetThicknessesCount(
   System.string ClassName,
   System.string MaterialName
)
```

### C++/CLI

```cpp
System.int GetThicknessesCount(
   System.String^ ClassName,
   System.String^ MaterialName
)
```

### Parameters

- `ClassName`: Name of the material class
- `MaterialName`: Name of the material

### Return Value

Number of sheet metal thicknesses for the specified material

## VBA Syntax

See [CostAnalysisSheetMetal::GetThicknessesCount](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~GetThicknessesCount.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
