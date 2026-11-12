---
title: "GetThicknessesCount Method (ICostAnalysisSheetMetal)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisSheetMetal"
member: "GetThicknessesCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetThicknessesCount.html"
---

# GetThicknessesCount Method (ICostAnalysisSheetMetal)

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
Dim instance As ICostAnalysisSheetMetal
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

[ICostAnalysisSheetMetal Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal.html)
[ICostAnalysisSheetMetal Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal_members.html)
[ICostAnalysisSheetMetal::GetThicknesses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetThicknesses.html)
[ICostAnalysisSheetMetal::IGetThicknesses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~IGetThicknesses.html)
[ICostAnalysisSheetMetal::CurrentThickness Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CurrentThickness.html)
[ICostAnalysisSheetMetal::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetMaterialClasses.html)
[ICostAnalysisSheetMetal::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetMaterials.html)
[ICostAnalysisSheetMetal::GetModelThickness Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~GetModelThickness.html)
[ICostAnalysisSheetMetal::IGetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~IGetMaterialClasses.html)
[ICostAnalysisSheetMetal::IGetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~IGetMaterials.html)
[ICostAnalysisSheetMetal::CurrentMaterial Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CurrentMaterial.html)
[ICostAnalysisSheetMetal::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisSheetMetal~CurrentMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
