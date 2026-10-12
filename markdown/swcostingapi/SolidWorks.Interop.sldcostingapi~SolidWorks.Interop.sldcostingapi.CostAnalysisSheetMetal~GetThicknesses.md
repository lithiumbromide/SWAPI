---
title: "GetThicknesses Method (CostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisSheetMetal"
member: "GetThicknesses"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal~GetThicknesses.html"
---

# GetThicknesses Method (CostAnalysisSheetMetal)

Gets the sheet metal thicknesses for the specified material from the Costing template for this sheet metal Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThicknesses( _
   ByVal ClassName As System.String, _
   ByVal MaterialName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisSheetMetal
Dim ClassName As System.String
Dim MaterialName As System.String
Dim value As System.Object

value = instance.GetThicknesses(ClassName, MaterialName)
```

### C#

```csharp
System.object GetThicknesses(
   System.string ClassName,
   System.string MaterialName
)
```

### C++/CLI

```cpp
System.Object^ GetThicknesses(
   System.String^ ClassName,
   System.String^ MaterialName
)
```

### Parameters

- `ClassName`: Name of the material class
- `MaterialName`: Name of the material

### Return Value

Array of doubles of the sheet metal thicknesses for the specified material

## VBA Syntax

See [CostAnalysisSheetMetal::GetThicknesses](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisSheetMetal~GetThicknesses.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal.html)
[CostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisSheetMetal_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
